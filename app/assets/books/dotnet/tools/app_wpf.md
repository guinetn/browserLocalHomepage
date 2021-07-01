# WPF

.NET Core UI framework for building Windows desktop applications.
Development features
- application model
- resources
- controls
- graphics
- layout
- data binding
- documents
- XAML (Extensible Application Markup Language): declarative model 
- vector graphics architecture (infinitely scaled)
- flexible hosting model (host a video in a button...).

WPF and WinForms applications 
- only run on Windows
- are part of the Microsoft.NET.Sdk.WindowsDesktop 

- https://docs.microsoft.com/en-us/windows/apps/
- https://docs.microsoft.com/en-us/dotnet/desktop/wpf/overview/?view=netdesktop-5.0
- https://github.com/dotnet/wpf
- https://github.com/Microsoft/WPF-Samples
- [good train](https://www.youtube.com/watch?v=oSeYvMEH7jc&t=1442s)

## start

```bash
dotnet new wpf -o MyWPFApp
cd MyWPFApp
dotnet run
```

### COMMANDS

Most Windows applications were built on an event-based model: controls ← wire up → event handlers (code-behind)
Data binding provided alternatives to the old event-driven system

Commands separate UI component (semantic) from the logic to execut on command invocation
You can test business logic separately using test cases and also your UI code is loosely coupled to business logic.

* ICommand 
System.Windows.Input
Generic implementation of a loosely coupled command.

- Coupling scenario
XAML is tightly coupled to the code behind due to the event handler declaration
```xml
<Button x Name="BtnFireEvent" Content="Fire" Click ="btnFireEvent_Click"/>
private void btnFireEvent_Click( object sender, RoutedEventArgs e) {
    MessageBox.Show("Hello Event Handler!"
}
```

- ICommand 
allow to implement a class to act as a generic command

***CanExecute()***  
A support method that returns a Boolean indicating whether the command is in an executable state. The WPF data binding mechanism will check the return value of this method and enable or disable the associated control based on the value.
***Execute()***  
A method that contains the code that should be executed to accomplish the task associated with the command.

Button.Command can be binded to an ICommand

```xml
<Window x:Class="WPFExample.ButtonClick" xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" Title="ButtonClick" Height="300" Width="300" xmlns:viewModel="clr-namespace:WPFCommand"> 
<Window.Resources> 
    <viewModel:CommandViewModel x:Key="commandViewModel" /> 
</Window.Resources> 
<Grid DataContext="{StaticResource ResourceKey=commandViewModel}"> 
<Button x:Name="btnFireEvent" Content="Fire event" Width="100" Height="100" 
    Command="{Binding Path=ButtonClickCommand}" 
    CommandParameter="{Binding}" /> 
</Grid> 
</Window>
```xml

```c#
namespace WPFCommand { 
    public class CommandViewModel { 
        public ICommand ButtonClickCommand { 
            get { 
                return new ButtonClickCommand(); 
            } 
        } 
        
        public void ShowMessagebox(string message) { 
            MessageBox.Show(message); 
        }

namespace WPFCommand { 
    public class ButtonClickCommand : ICommand { 
        public bool CanExecute(object parameter) { return true; } 
        public event EventHandler CanExecuteChanged; 
        public void Execute(object parameter) { 
            var viewModel = (CommandViewModel)parameter;
            viewModel.ShowMessagebox("Hello decoupled command!");

event EventHandler CanExecuteChanged;    // invoked when changes occur that can change whether or not the command can be executed.
bool CanExecute(object parameter);       // whether the command can be executed or not
void Execute(object parameter);          // Runs the command logic
```

But it does not allow to have a different logic for CanExecute or Execute
Each command needs to implement a new class... Fix is RelayCommand implementation: a command that can be instantiated passing the actions to be executed
```cs
public class NormalCommand : ICommand    
{    
    public event EventHandler CanExecuteChanged;    
     
    public bool CanExecute(object parameter)    
    {    
        throw new NotImplementedException();    
    }    
     
    public void Execute(object parameter)    
    {    
        throw new NotImplementedException();    
    }    
}   
```

* DelegateCommand

```cs
    /// <summary>
    /// Represents a command that forwards the <c>Execute</c> and <c>CanExecute</c> calls to specified delegates.
    /// </summary>
    public class DelegateCommand<T> : ICommand
    {
        private readonly Action<T> _executeCallback;
        private readonly Predicate<T> _canExecuteCallback;

        /////////////////////////////////////////////////////////////////////////////////////////////////////
        // OBJECT
        /////////////////////////////////////////////////////////////////////////////////////////////////////

        /// <summary>
        /// Initializes a new instance of the <see cref="DelegateCommand<T>"/> class.
        /// </summary>
        /// <param name="executeCallback">The execute callback delegate.</param>
        public DelegateCommand(Action<T> executeCallback)
            : this(executeCallback, null)
        {
            // No-op
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="DelegateCommand<T>"/> class.
        /// </summary>
        /// <param name="executeCallback">The execute callback delegate.</param>
        /// <param name="canExecuteCallback">The can execute callback delegate.</param>
        public DelegateCommand(Action<T> executeCallback, Predicate<T> canExecuteCallback)
        {
            if (executeCallback == null)
                throw new ArgumentNullException("executeCallback");

            this._executeCallback = executeCallback;
            this._canExecuteCallback = canExecuteCallback;
        }

        /////////////////////////////////////////////////////////////////////////////////////////////////////
        // INTERFACE IMPLEMENTATION
        /////////////////////////////////////////////////////////////////////////////////////////////////////

        #region ICommand Members

        /// <summary>
        /// Defines the method that determines whether the command can execute in its current state.
        /// </summary>
        /// <param name="parameter">Data used by the command.  If the command does not require data to be passed, this object can be set to <see langword="null"/>.</param>
        /// <returns>
        /// <c>true</c> if this command can be executed; otherwise, <c>false</c>.
        /// </returns>
        public bool CanExecute(object parameter)
        {
            return (this._canExecuteCallback == null) ? true : this._canExecuteCallback((T)parameter);
        }

        /// <summary>
        /// Occurs when changes occur that affect whether or not the command should execute.
        /// </summary>
        public event EventHandler CanExecuteChanged
        {
            add
            {
                if (this._canExecuteCallback != null)
                    CommandManager.RequerySuggested += value;
            }
            remove
            {
                if (this._canExecuteCallback != null)
                    CommandManager.RequerySuggested -= value;
            }
        }

        /// <summary>
        /// Defines the method to be called when the command is invoked.
        /// </summary>
        /// <param name="parameter">Data used by the command.  If the command does not require data to be passed, this object can be set to <see langword="null"/>.</param>
        public void Execute(object parameter)
        {
            this._executeCallback((T)parameter);
        }

        #endregion // ICommand Members

    }
}
```

* RelayCommand

Bind commands directly to the ViewModels (avoid writing code in the views codebehind)
Specify what to execute at command creation: no need to implement a new class for each different action to take
You have to provide two methods
- Execute()
- CanExecute()
 
```C#
var cmd1 = new RelayCommand(o => { /* do something 1 */ }, o => true);    
var cmd2 = new RelayCommand(o => { /* do something 2 */ }, o => true);   
```

```C#
public RelayCommand MyCommand 
{ 
  get; 
  private set; 
}   
public MainViewModel() 
{ 
  MyCommand = new RelayCommand( ExecuteMyCommand, () => _canExecuteMyCommand); 
}   
private void ExecuteMyCommand() { // Do something }
```

CommandManager.RequerySuggested handles events when something in the interface suggests that a requery should happen. 
If your ICommand adds the handlers to it then it will automatically update UI elements when the screen executes some actions. (For example, lose focus on a TextBox.)

```C#
public class RelayCommand : ICommand    
{    
    private Action<object> execute;    
    private Func<object, bool> canExecute;    
     
    public event EventHandler CanExecuteChanged    
    {    
        add { CommandManager.RequerySuggested += value; }    
        remove { CommandManager.RequerySuggested -= value; }    
    }    
     
    public RelayCommand(Action<object> execute, Func<object, bool> canExecute = null)    
    {    
        this.execute = execute;    
        this.canExecute = canExecute;    
    }    
     
    public bool CanExecute(object parameter)    
    {    
        return this.canExecute == null || this.canExecute(parameter);    
    }    
     
    public void Execute(object parameter)    
    {    
        this.execute(parameter);    
    }    
}  
```

```xml
<CheckBox Content="CheckBox"
          Command="{Binding YourCommand}"
          CommandParameter="{Binding IsChecked, RelativeSource={RelativeSource Self}}" />
          CommandParameter="{Binding IsChecked, RelativeSource={RelativeSource Self}, Mode=OneWay}

<CheckBox Content="{Binding Path=Name}"
          CommandParameter="{Binding}"
          Command="{Binding DataContext.AddRemovePresetAssignmentCommand,
          RelativeSource={RelativeSource FindAncestor,
                           AncestorType={x:Type UserControl}}}">
```
                    
MVVM

XAML's namespaces:
xmlns:t="http://schemas.telerik.com/2008/xaml/presentation" 
xmlns:i="http://schemas.microsoft.com/expression/2010/interactivity"          Add System.Windows.Interactivity in project references

```xml
<CheckBox IsChecked="{Binding ServiceOrderItemTask.IsCompleted, Mode=TwoWay}" Content="{Binding ServiceOption.Name}">

    <i:Interaction.Triggers>
          <i:EventTrigger EventName="Checked">
                 <i:InvokeCommandAction Command="{Binding DataContext.IsCompletedCheckedCommand, RelativeSource={RelativeSource FindAncestor, AncestorType={x:Type t:RadGridView}}}" CommandParameter="{Binding}"/>
           </i:EventTrigger>

           <i:EventTrigger EventName="Unchecked">
                 <i:InvokeCommandAction Command="{Binding DataContext.IsCompletedUncheckedCommand, RelativeSource={RelativeSource FindAncestor, AncestorType={x:Type t:RadGridView}}}" CommandParameter="{Binding}"/>
           </i:EventTrigger>
    </i:Interaction.Triggers>
              
<CheckBox IsChecked="{Binding SomeBoolProperty, Mode=OneWay}" Content="Check Meee!">
    <i:Interaction.Triggers>
        <i:EventTrigger EventName="Checked">
            <i:InvokeCommandAction Command="{Binding MyOnCheckedCommand}"/>
        </i:EventTrigger>
        <i:EventTrigger EventName="Unchecked">
            <i:InvokeCommandAction Command="{Binding MyOnUncheckedCommand}"/>
        </i:EventTrigger>
    </i:Interaction.Triggers>
</CheckBox>
```

implement INotifyPropertyChanged on the ViewModel 

```c#
public event PropertyChangedEventHandler PropertyChanged;
private void OnPropertyChanged(string name) => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));

private bool _SomeBoolProperty = false;
public bool SomeBoolProperty { 
    get => _SomeBoolProperty;
    set { 
        _SomeBoolProperty = value; 
        OnPropertyChanged(nameof(SomeBoolProperty)); 
    } 
}

public ICommand MyOnCheckedCommand { get; } = new RelayCommand(o => { SomeBoolProperty = true; });
public ICommand MyOnUncheckedCommand { get; } = new RelayCommand(o => { SomeBoolProperty = false;});
```

* Existing commands
     
ApplicationCommands   
Close, Copy, Cut, Delete, Find, Help, New, Open, Paste, Print, PrintPreview, Properties, Redo, Replace, Save, SaveAs, SelectAll, Stop, Undo, and more.

ComponentCommands   
MoveDown, MoveLeft, MoveRight, MoveUp, ScrollByLine, ScrollPageDown, ScrollPageLeft, ScrollPageRight, ScrollPageUp, SelectToEnd, SelectToHome, SelectToPageDown, SelectToPageUp, and more.

MediaCommands  
ChannelDown, ChannelUp, DecreaseVolume, FastForward, IncreaseVolume, MuteVolume, NextTrack, Pause, Play, PreviousTrack, Record, Rewind, Select, Stop, and more.

NavigationCommands   
BrowseBack, BrowseForward, BrowseHome, BrowseStop, Favorites, FirstPage, GoToPage, LastPage, NextPage, PreviousPage, Refresh, Search, Zoom, and more.

EditingCommands   
AlignCenter, AlignJustify, AlignLeft, AlignRight, CorrectSpellingError, DecreaseFontSize, DecreaseIndentation, EnterLineBreak, EnterParagraphBreak, IgnoreSpellingError, IncreaseFontSize, IncreaseIndentation, MoveDownByLine, MoveDownByPage, MoveDownByParagraph, MoveLeftByCharacter, MoveLeftByWord, MoveRightByCharacter, MoveRightByWord and more.

## Logical tree vs. visual tree
## Templates     
Templates allow you to change the appearance as well as the behavior of your controls

Each WPF control has a “lookless” design. This means that the look of the control can be completely changed from its default appearance. The behavior of the control is baked into the classes that represent the control, and the appearance is defined by what is known as a control template

```xml
<Window.Resources> 
    <ControlTemplate x:Key="CustomButtonTemplate" TargetType="{x:Type Button}"> 
        <Border Name="Border" BorderBrush="Blue" BorderThickness="3" CornerRadius="2" Background="BlueViolet" TextBlock.Foreground="White"> 
        <Grid> 
            <Rectangle Name="FocusCue" Visibility="Hidden" Stroke="Black">
            ...
    <ControlTemplate.Triggers> 
        <Trigger Property="IsMouseOver" Value="True"> 
            <Setter TargetName="Border" Property="Background" Value="DarkBlue" /> 
        </Trigger> 
        <Trigger Property="IsPressed" Value="True"> 
            <Setter TargetName="Border" Property="Background" Value="Purple" /> 
            <Setter TargetName="Border" Property="BorderBrush" Value="DarkKhaki" /> 
        </Trigger>
</Window.Resources> 
<Grid> 
<Button Width="100" Height="30" Margin="10" Template="{StaticResource CustomButtonTemplate}">Button Template in action</Button>
```xml

## Data templates

```xml
<ListBox Name="lstProducts" Width="300" Height="200"> 
    <ListBox.ItemTemplate> 
        <DataTemplate> 
            <Border BorderThickness="3" CornerRadius="6" BorderBrush="AliceBlue" Background="DarkBlue">
            <TextBlock Grid.Column="1" Grid.Row="0" x:Name="txtProductName" Text="{Binding ProductName}" Foreground="White" />
```

```c#
public partial class MainWindow : Window { 
    public ProductViewModel ViewModel { get; set; }       
    InitializeComponent(); 
    ViewModel = new ProductViewModel(); 
    lstProducts.DataContext = ViewModel; 
    lstProducts.ItemsSource = ViewModel;     

public class Product : INotifyPropertyChanged { 
    private string _productName; 
    private string _productPrice;
        
namespace BindObservableCollectionToListbox {
    public class ProductViewModel : ObservableCollection<Product> { 
        public ProductViewModel() { 
            this.Add(new Product { ProductName = "Toy Truck", ProductPrice = "$20.99"}); 
            this.Add(new Product { ProductName = "Baseball Glove", ProductPrice = "$4.99"}); 
            this.Add(new Product { ProductName = "Baseball Bat", ProductPrice = "$7.99" }); 
        } 
    } 
}
```

## Triggers
used in styles and templates to change a control's property when another property value is changed
To respond to IsMouseOver, IsPressed, IsKeyboardFocused

#### DependencyProperty 


#### MVVM Pattern:
View (UI:xaml) <---> ViewModel (Binds view to model) <---> Model (Data)

***View***
```xml
<Window x:Class="WpfSimple.MainWindow"  
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"  
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"  
        xmlns:local="clr-namespace:WpfSimple"  
        Title="MainWindow" Height="150" Width="370">  
    <Window.DataContext>  
        <local:MainWindowViewModel/>  
    </Window.DataContext>  
        <Grid>  
        <Button Content="Click"  
                Height="23"  
                HorizontalAlignment="Left"  
                Margin="77,45,0,0"  
                Name="btnClick"  
                VerticalAlignment="Top"  
                Width="203"  
                Command="{Binding ButtonCommand}"  
                CommandParameter="Hai" />  
    </Grid>  
</Window>  
```

***ViewModel***
```C#
using System;  
using System.Collections.Generic;  
using System.Linq;  
using System.Text;  
using System.Windows.Input;  
using System.Windows;  
  
namespace WpfSimple  
{  
    class MainWindowViewModel  
    {  
        private ICommand m_ButtonCommand;  
        public ICommand ButtonCommand  
        {  
            get { return m_ButtonCommand; }  
            set { m_ButtonCommand = value; }  
        }  
        public MainWindowViewModel()  
        {  
            ButtonCommand = new RelayCommand(new Action<object>(ShowMessage));  
        }  
        public void ShowMessage(object obj) { MessageBox.Show(obj.ToString()); }  
    }  
}  
```

***RelayCommand***
```C#
using System;  
using System.Collections.Generic;  
using System.Linq;  
using System.Text;  
using System.Windows.Input;  
  
namespace WpfSimple  
{  
    class RelayCommand : ICommand  
    {  
        private Action<object> _action;  
        public RelayCommand(Action<object> action)  
        {  
            _action = action;  
        }  
        #region ICommand Members  
        public bool CanExecute(object parameter)  
        {  
            return true;  
        }  
        public event EventHandler CanExecuteChanged;  
        public void Execute(object parameter)  
        {  
            if (parameter != null)  
            {  
                _action(parameter);  
            }  
            else  
            {  
                _action("Hello World");  
            }  
        }  
        #endregion  
    }  
}  
```

```C#
public partial class App : Application  
{  
    protected override void OnStartup(StartupEventArgs e)  
    {  
        base.OnStartup(e);  
        WpfMvvmTest.MainWindow window = new MainWindow();  
        ProductViewModel VM = new ProductViewModel();  
        window.DataContext = VM;  
        window.Show();  
    }  
}  

class ProductViewModel  
{  
    private IList<Product> m_Products;  
    public ProductViewModel()  
    {  
        m_Products = new List<Product>  
        {  
            new Product {ID=1, Name ="Pro1", Price=10},  
            new Product{ID=2, Name="BAse2", Price=12}  
        };  
    }  
    public IList<Product> Products  
    {  
        get { return m_Products; }  
        set { m_Products = value; }  
    }  
    private ICommand mUpdater;  
    public ICommand UpdateCommand  
    {  
        get  
        {  
            if (mUpdater == null)  
                mUpdater = new Updater();  
            return mUpdater;  
        }  
        set  
        {  
            mUpdater = value;  
        }  
    }  
    private class Updater : ICommand  
    {  
        #region ICommand Members  
        public bool CanExecute(object parameter)  
        {  
            return true;  
        }  
        public event EventHandler CanExecuteChanged;  
        public void Execute(object parameter)  
        {  
        }  
        #endregion  
    }  
}  
```

```xml
<Window x:Class="WpfMvvmTest.MainWindow"  
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"  
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"  
        Title="MainWindow" Height="350" Width="525">  
    <Grid Height="314">  
        <Grid.RowDefinitions>  
            <RowDefinition Height="Auto"/>  
            <RowDefinition Height="*"/>  
            <RowDefinition Height="Auto"/>  
        </Grid.RowDefinitions>  
        <ListView Name="ListViewEmployeeDetails" Grid.Row="1" Margin="4,109,12,23"  ItemsSource="{Binding Products}"  >  
            <ListView.View>  
                <GridView x:Name="grdTest">  
                    <GridViewColumn Header="ID" DisplayMemberBinding="{Binding ID}"  Width="100"/>  
                    <GridViewColumn Header="Name" DisplayMemberBinding="{Binding Name}"  Width="100" />  
                    <GridViewColumn Header="Price" DisplayMemberBinding="{Binding Price}" Width="100" />  
                </GridView>  
            </ListView.View>  
        </ListView>  
        <TextBox Grid.Row="1" Height="23" HorizontalAlignment="Left" Margin="80,7,0,0" Name="txtID" VerticalAlignment="Top" Width="178" Text="  
Binding ElementName=ListViewEmployeeDetails,Path=SelectedItem.ID}" />  
        <TextBox Grid.Row="1" Height="23" HorizontalAlignment="Left" Margin="80,35,0,0" Name="txtName" VerticalAlignment="Top" Width="178" Text="{Binding ElementName=ListViewEmployeeDetails,Path=SelectedItem.Name}" />  
        <TextBox Grid.Row="1" Height="23" HorizontalAlignment="Left" Margin="80,61,0,0" Name="txtPrice" VerticalAlignment="Top" Width="178" Text="{Binding ElementName=ListViewEmployeeDetails,Path=SelectedItem.Price}" />  
        <Label Content="ID" Grid.Row="1" HorizontalAlignment="Left" Margin="12,12,0,274" Name="label1" />  
        <Label Content="Price" Grid.Row="1" Height="28" HorizontalAlignment="Left" Margin="12,59,0,0" Name="label2" VerticalAlignment="Top" />  
        <Label Content="Name" Grid.Row="1" Height="28" HorizontalAlignment="Left" Margin="12,35,0,0" Name="label3" VerticalAlignment="Top" />  
        <Button Content="Update" Grid.Row="1" Height="23" HorizontalAlignment="Left" Margin="310,40,0,0" Name="btnUpdate"  
                VerticalAlignment="Top" Width="141"  
                Command="{Binding Path=UpdateCommad}"  
                />  
    </Grid>  
</Window>  
```


#### INotifyPropertyChanged

Notify clients (binded clients) when a property value has changed
INotifyPropertyChanged contains an event called PropertyChanged

#### 
```C#
public class Product:INotifyPropertyChanged  
{  
    private int m_ID;  
    private string m_Name;  
    private double m_Price;  
    #region INotifyPropertyChanged Members  
    public event PropertyChangedEventHandler PropertyChanged;  
    private void OnPropertyChanged(string propertyName)  
    {  
        if (PropertyChanged != null)  
        {  
            PropertyChanged(this, new PropertyChangedEventArgs(propertyName));  
        }  
    }  
    #endregion  
  
    public int ID  
    {  
        get { return m_ID; }  
        set { m_ID = value; OnPropertyChanged("ID");  
        }  
    }  
    public string Name  
    {  
        get { return m_Name; }  
        set { m_Name = value; OnPropertyChanged("Name");  
        }  
    }  
    public double Price  
    {  
        get { return m_Price; }  
        set { m_Price = value; OnPropertyChanged("Price");  
        }  
    }  
}  
```

#### RoutedCommand 

Defines a command that implements ICommand and is routed through the element tree.
Execute and CanExecute methods on a RoutedCommand do not contain the application logic for the command as is the case with a typical ICommand, but rather, these methods raise events that ***traverse the element tree looking for an object with a CommandBinding***. The event handlers attached to the CommandBinding contain the command logic.

Execute method raises the PreviewExecuted and Executed events. 
CanExecute method raises the PreviewCanExecute and CanExecute events.

* RoutedUICommand 
Defines an ICommand that is routed through the element tree and contains a text property.
RoutedUICommand includes a Text property (RoutedUICommand not)

https://docs.microsoft.com/en-gb/dotnet/api/system.windows.input.routedcommand?view=net-5.0

#### ----

Achieving the same marshalling check on the Windows Presentation Foundation (WPF) platform involves a slightly different approach. WPF includes a static member property called Current of type DispatcherObject on the System.Windows.Application class. Calling CheckAccess() on the dispatcher serves the same function as InvokeRequired on controls in Windows Forms.

Below this approach with a static UIAction object. Whenever a developer wants to call a method that might interact with the user interface, she simply calls UIAction.Invoke() and passes a delegate for the UI code she wishes to call. This, in turn, checks the dispatcher to see if marshalling is necessary and responds accordingly.

One additional feature in the UIAction of Listing 12 is the marshalling of any exceptions on the UI thread that may have occurred. SafeInvoke() wraps all requested delegate calls in a try/catch block; if an exception is thrown, it saves the exception and then rethrows it once the context returns to the calling thread. In this way, UIAction avoids throwing unhandled exceptions on the UI thread.

Safely Invoking User Interface Objects

```cs
using System;
using System.Windows;
using System.Windows.Threading;

public static class UIAction
{
    public static void Invoke<T>(
    
    Action<T> action, T parameter) { Invoke(() => action(parameter)); }
    
    public static void Invoke(Action action)
    {
        DispatcherObject dispatcher = Application.Current; 
        if (dispatcher == null || dispatcher.CheckAccess() || dispatcher.Dispatcher == null ) 
            { action(); }
        else
        { SafeInvoke(action); }
    }
    
    // We want to catch all exceptions here so we can rethrow them.
    private static void SafeInvoke(Action action)
    {
        Exception exceptionThrown = null;
        Action target = () => { 
            try {
                action();
            }
            catch (Exception exception) {
                exceptionThrown = exception;
            }    
        };
        
        Application.Current.Dispatcher.Invoke(target);
        if (exceptionThrown != null)
        {
            // Use ExceptionDispatchInfo.Throw() for .NET 4.5+.
            throw exceptionThrown;
        }
    }
    
}

```

## XAML - Extensible Application Markup Language “Zammel”

allows the user interface to be completely independent from the logic in the code behind.
WPF assembly namespaces start with 'System.Windows'

By specifying the URI, the code will search each of the namespaces and automatically resolve that the Window element maps to the System.Windows.Window class. It will find the Grid resides in the System.Windows.Controls assembly namespace

```xml
<Window 
x:Class="Chapter01.MainWindow"   ← Window’s class name (code behind in to access the window programmatically)
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"    ← defines standard WPF controls (default XAML namespace, no prefix needed for elements inside)
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"  ← utility classes, dictate how your XAML document is interpreted
This namespace has 'x' suffix: to access elements of this namespace, we will prefix the element with x:. 
For example, <x:MyElement> <x:string> <Buton x:Name="button1">
Title="MainWindow" Height="134" Width="515"> 
xmlns:x attribute indicates an additional XAML namespace, which maps the XAML language namespace http://schemas.microsoft.com/winfx/2006/xaml.

xmlns:mc="http://schemas.openxmlformats.org/markup compatibility/2006"
xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
mc:Ignorable="d"
d:DesignHeight="300" d:DesignWidth="300" 
Height="350" Width="300" Background="White"
>
<Grid> 
    <Grid.RowDefinitions> 
        <RowDefinition Height="36*" /> 
        <RowDefinition Height="91*" /> 
    </Grid.RowDefinitions> 
    <Grid.ColumnDefinitions> 
    <ColumnDefinition /> 
        <ColumnDefinition /> 
    </Grid.ColumnDefinitions> 
    <Label Grid.Row="0" Grid.Column="0" Content="Rendering Tier" /> 
    <TextBox Grid.Row="0" Grid.Column="1" x:Name="txtRenderingTier" /> 
    <Button x:Name="btnGetRenderingTier" Content="Get Rendering Tier" Grid.Row="1" Grid.Column="1" Width="130" Height="30" Click="btnGetRenderingTier_Click" /> 
</Grid> 
</Window>
```xml

```c#
using System.Windows; 
using System.Windows.Media; 
namespace Chapter01 { 
    /// <summary> 
    /// Interaction logic for MainWindow.xaml. 
    /// </summary> 
    
    public partial class MainWindow : Window { 
        public MainWindow() { 
            InitializeComponent(); 
        } 
        private void btnGetRenderingTier_Click(object sender, RoutedEventArgs e) 
        {
            txtRenderingTier.Text = string.Format("{0} Partial hardware acceleration.", 2);
        }
    }
}
```

### XAML attributes
specified as strings, many properties must be converted to a more complex data type  by a class called System.ComponentModel.TypeConverter

### default WPF controls
- Button
    Button, ToggleButton, CheckBox, RadioButton
- Text
    TextBlock: a block of text that cannot be edited (~Label)
- Shapes
- Containers
Grid: 
    - Fixed: (size of logical units (1/96 inch)
    - Auto: Takes as much space as needed by the contained control.
    - *: Takes as much space as available (after filling all auto and fixed sized columns), proportionally divided over all star-sized columns. So 3*/5* means the same as 30*/50*. Remember that star sizing does not work if the grid size is calculated based on its conten
StackPanel
    Orientation=Vertical/Horizontal
    WPF ItemsControls like ComboBox, ListBox, Menu use a StackPanel as their internal layout panel
DockPanel
    Orientation=Vertical/Horizontal

```xml
<DockPanel LastChildFill="True">
<Button Content="" DockPanel.Dock="Top"> Bottom / Left / Right
```
WrapPanel
Orientation=Vertical/Horizontal
It does not stack all child elements to one row. It wraps them to new lines if no space is left in the width of the container
Canvas

```xml
<Canvas> 
    <Rectangle Canvas.Left="40" Canvas.Top="31" Width="63" Height="41" Fill="Blue" /> 
    <Ellipse Canvas.Left="130" Canvas.Top="79" Width="58" Height="58" Fill="Blue" /> 
    <Path Canvas.Left="61" Canvas.Top="28" Width="133" Height="98" Fill="Blue" Stretch="Fill" Data="M61,125 L193,28"/> 
</Canvas>    
```
    
Layout best practices
* Avoid fixed positions; instead, use the Alignment properties in combination with Margins to position elements in a panel.
* Avoid fixed sizes. Set the Width and Height of elements to Auto whenever possible.
* Don't use the Canvas panel to specify the layout of common controls; instead use it to arrange vector graphics.
* Use a StackPanel to lay out dialog confirmation buttons on a dialog.
* Use a Grid to lay out complex user interfaces and data entry forms.
- Media
- Toolbars
- Scrolls
- Panels and lists


## Type Converters

System.ComponentModel.TypeConverter class provides a unified way of converting XAML string attribute values to corresponding object value types.

***CanConvertTo()***  
A support method that returns a Boolean indicating whether the value can be converted to the specified type.

***CanConvertFrom()***  
A support method that returns a Boolean indicating whether the value can be converted from a specified type.

***ConvertTo()***  
Converts the given value object to the specified type.

***ConvertFrom()***  
Converts the given value to the type of this converter

## Data binding
Process that establishes a connection between the application UI and the business logic.
If the binding has the correct settings and the data provides the proper notifications, when the data changes its value, the elements that are bound to the data reflect changes automatically

***OneWay***   
binding causes changes to the source property to automatically update the target property, but changes to the target property are not propagated back to the source property.

***TwoWay***   
binding causes changes to either the source property or the target property to automatically update the other
TextBox.Text and CheckBox.IsChecked default to TwoWay binding
A programmatic way to determine whether a dependency property binds one-way or two-way by default is to get the property metadata using GetMetadata and the

***OneWayToSource***   
Reverse of OneWay binding; it updates the source property when the target property changes. One example scenario is if you only need to re-evaluate the source value from the UI.

***OneTime***   
Causes the source property to initialize the target property, but subsequent changes do not propagate. This means that if the data context undergoes a change or the object in the data context changes, then the change is not reflected in the target property.

## DataContext
Binding object needs a data source
Binding.Source=...
DataContext, attached property, can be set at the Window level and propagate down to each data-bound control by way of property value inheritance. 
ElementName
RelativeSource 
User interface elements in WPF have a DataContext attached property. That property has the standard dependency property value inheritance behavior by default. This means if you set the DataContext on an element to a Student object, the DataContext property on all of the parent’s logical descendant elements will inherit the Student object reference. This means that all data bindings contained within the root element’s tree will automatically bind against the Student object, unless explicitly told to bind against something else.

## Resource dictionaries
You can create a resource dictionary at the Application, Window, and UserControl levels. A XAML dictionary contains elements known as resources. This essentially allows you to import your own C# objects to use in XAML data binding.

## INotifyPropertyChanged

```c#
namespace SimpleData-binding {
    public class Person : INotifyPropertyChanged { 

    private string _FirstName; 
    private string _LastName; 
    private string _FullName;

    public string FirstName { 
        get { return _FirstName; } 
        set { 
                if (_FirstName != value) { 
                    _FirstName = value; 
                    this.FullName = string.Format("{0} {1}", _FirstName, _LastName); // Update FullName. Repeat code for LastName...
                    OnPropertyChanged("FirstName"); 
                } 
            } 
        }    
        
    public event PropertyChangedEventHandler PropertyChanged; 
    private void OnPropertyChanged(string propertyName) { 
        var handler = PropertyChanged; 
        if (handler != null) { 
            handler(this, new PropertyChangedEventArgs(propertyName)); 
        } 
}
```

```xml    
<TextBox Name="txtFirstName" Grid.Column="1" Grid.Row="1" FontSize="20" Text="{Binding Path=FirstName}" />   
<TextBox Name="txtLastName" Grid.Column="1" Grid.Row="2" FontSize="20" Text="{Binding Path=LastName}" /> 
<TextBlock Name="txtFullName" Grid.Column="1" Grid.Row="3" FontSize="20" Text="{Binding Path=FullName}" />
```

```c#
public partial class MainWindow : Window { 
    private Person _person; 
    
    public MainWindow() { 
        InitializeComponent();
        //Create an instance of the Person object. 
        _person = new Person {FirstName = "<Enter first name>", LastName = "<Enter last name>" }; 
        //Set the DataContext of the Window. 
        this.DataContext = _person; 
    } 
    
    private void btnClose_Click(object sender, RoutedEventArgs e) { this.Close(); }
```

## MultiBinding

involves creating an IMultiValueConverter and binding the converter to the txtFullName element. The IMultiValueConverter interface works just like the IValueConverter interface except that it accepts an array of values to convert. The array of values comes from the element properties that we define in the MultiBinding xaml definition. A brief example will make things clearer

```xml
<Window x:Class="MultiBinding.MainWindow" 
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" 
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 
Title="MainWindow" Height="218.905" Width="525" 
xmlns:tc="clr-namespace:MultiBinding"> 
<Window.Resources> 
    <tc:FullnameConverter x:Key="fullNameConverter" /> 
</Window.Resources>
```

```c#
using System; 
using System.Collections.Generic; 
using System.Linq; 
using System.Text; 
using System.Threading.Tasks; 
using System.Windows.Data; 
namespace MultiBinding { 
/// <summary> 
/// This class is a MultiValueConverter. It works much like a ValueConverter, except that it takes an array of values in the convert 
/// method and it returns an array of values from the ConvertBack routine. 
/// </summary> 
public class FullnameConverter : IMultiValueConverter 
{ 
    public object Convert(object[] values, Type targetType, object parameter, System.Globalization.CultureInfo culture) { 
        StringBuilder fullNameBuilder = new StringBuilder(); 
        foreach (object name in values) { 
            fullNameBuilder.AppendFormat("{0} ", name.ToString()); 
        } 
        return fullNameBuilder.ToString(); 
    } 
    
    public object[] ConvertBack(object value, Type[] targetTypes, object parameter, System.Globalization.CultureInfo culture) 
    { 
        throw new NotImplementedException(); 
    } 
} 

}
```

```xml
<TextBox Name="txtFirstName" Grid.Column="1" Grid.Row="1" FontSize="20" Text="{Binding Path=FirstName}" />
<TextBox Name="txtFullName" Grid.Column="1" Grid.Row="3" FontSize="20"> 
    <TextBox.Text> 
        <MultiBinding Converter="{StaticResource fullNameConverter}"> 
            <Binding ElementName="txtFirstName" Path="Text" /> 
            <Binding ElementName="txtLastName" Path="Text" /> 
        </MultiBinding> 
    </TextBox.Text> 
</TextBox>
```

## MVVM - Model-View-ViewModel 

Separate the user interface from the logic required to facilitate the user interface and the business logic and data. Separation of UI, business logic, and data allows for a nice, clean, testable piece of software.

***Model***  
The Model represents the data that you wish to interact with. implement the INotifyPropertyChanged
***ViewModel***   
Class with properties that point to your model's properties. Use Data binding to bind to ViewModel.
***Views***  
WPF Windows or UserControls

```c#
public class Contact : INotifyPropertyChanged { 
    private string _firstName;
    private string _lastName;
    ...
    public string FirstName { get { return _firstName; } set { _firstName = value; OnPropertyChanged("FirstName"); ...
    
    public event PropertyChangedEventHandler PropertyChanged; // This will cause an event to notify WPF via data-binding that a change has occurred. 
    private void OnPropertyChanged(string propertyName) {...}
}
```

## ObservableCollection
WPF data binding knows when items are added or removed.

Bind a ListView's ItemsSource property to the ViewModel as well as bind the main grid's DataContext property to the ViewModel. By setting the DataContext of the top-level grid, we will cause the child controls to inherit the DataContext for data binding. The ItemsSource property of the ListView will populate the ListView with each item that exists in our ObservableCollection

```c#
public class ContactManagerViewModel : ObservableCollection<Contact> {
    public ContactManagerViewModel() { PrepareContactCollection(); } 
    private void PrepareContactCollection() { 
    var ContactOne = new Contact { FirstName = "John", LastName = "Doe", EmailAddress = "jdoe@email.com", TelephoneNumber = "555-555-5555" }; 
    Add(ContactOne); 
    // inheriting from ObservableCollection<Contact> we gain an Add() method. This allows us to populate the ViewModel with instances of our Contact Model.
}
```

```xml
<Window 
x:Class="ExceptionValidation.ContactManager" 
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" 
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 
Title="ContactManager" Height="300" Width="300" 
xmlns:viewModel="clr-namespace:ContactMvvm"> 
<Window.Resources> 
    <viewModel:ContactManagerViewModel x:Key="contactViewModel" /> 
</Window.Resources> 
<Grid DataContext="{StaticResource ResourceKey=contactViewModel}">    
<ListView Grid.ColumnSpan="2" BorderThickness="2" x:Name="lstContacts" 
IsSynchronizedWithCurrentItem="True" 
ItemsSource="{StaticResource ResourceKey=contactViewModel}" 
DisplayMemberPath="FirstName" Margin="0,0,0,28" Grid.RowSpan="2" />
>
<TextBlock Grid.Column="0" Grid.Row="1" Text="First name" />
<TextBox Grid.Column="1" Grid.Row="1" Text="{Binding Path=FirstName}" /> 
<TextBox Grid.Column="1" Grid.Row="2" Text="{Binding Path=LastName}" />
```

## 

## TERMS
Object: The base class for all .NET classes.
DispatcherObject: This is a base class for any object that can only be accessed on the thread for which the object was created. Most WPF classes derive from DisaptcherObject, so naturally the ones that do are not thread-safe.
DependencyObject: This is the base class for any object that has the ability to support DependencyProperties.
DependencyProperties: The base class provides the GetValue and SetValue methods, which DependencyProperties must use in order to work.
Freezable: The base class for all objects that can be “frozen” into a read-only state. Once frozen, they cannot be unfrozen.
Visual: The base class for all objects that have a visual representation.
UIElement: The base class for all visual objects with support for routed events, command binding, layout, and focus support.
ContentElement: A base class similar to UIElement but for pieces of content that don't have rendering behavior on their own. Instead, ContentElements are hosted in a Visual-derived class to be rendered on the screen.
FrameworkElement: The base class that adds support for styles, data binding, resources, and a few common mechanisms for Windows-based controls such as tooltips and context menus.
FrameworkContentElement: The analog to FrameworkElement for content.
Control: The base class for familiar controls such as Button, ListBox, and StatusBar. Control adds many properties to its FrameworkElement base class, such as Foreground, Background, and FontSize. Controls also support templates that enable you to completely replace their visual tree.

## Tools

xaml-controls-gallery ***
https://www.microsoft.com/en-us/p/xaml-controls-gallery/9msvh128x2zt?activetab=pivot:overviewtab

Fluent XAML Theme Editor
https://www.microsoft.com/en-us/p/fluent-xaml-theme-editor/9n2xd3q8x57c?activetab=pivot%3Aoverviewtab

Blend
allows a designer to create extremely complex and stunning visual effects oriented to WPF XAML user interfaces

Snoop 
Examining complex user interfaces
to attach to any WPF application to view and modify the visual tree's elements and their properties

SignTool
C:\Program Files (x86)\Microsoft SDKs\ClickOnce\SignTool

## Prism framework
Building modular WPF composite applications
Part of Microsoft's patterns and practices suite of software
Classes to create loosely coupled modules that are dynamically loaded and displayed inside of a main shell
The shell is divided into regions, which you dynamically fill with user control views that are found in your modules


## MODERN WPF UI
- https://www.youtube.com/watch?v=PzP8mw7JUzI&t=679s
- https://www.youtube.com/watch?v=fzBcXicj2G8&t=630s
- https://www.youtube.com/watch?v=YkZq3u9gmRc&t=76s

## More
- https://intellitect.com/interfacing-multithreading-patterns/
- https://github.com/Code52/Enhance
- https://www.codeproject.com/Tips/5294830/WPF-with-PRISM-View-and-ViewModel-First-Implementa
- https://www.youtube.com/watch?v=3ox-6NFAt8I&t=3s
- https://www.youtube.com/watch?v=fehVTLNQorQ&t=1s
- [Relay commands](https://www.youtube.com/watch?v=8WfD2cFRymM&t=306s)
- [WPF Introduction](https://www.youtube.com/watch?v=WYBoTT2ce8c)
- [WPF Introduction](https://www.youtube.com/watch?v=gSfMNjWNoX0&t=375s)
- [Relative source + debug](https://www.youtube.com/watch?v=QLEvT0vMrdc)
- https://www.youtube.com/channel/UCWo4JEf0ZBxU2qXtRMfs8Xw
- https://www.youtube.com/watch?v=_3R_8mXqhnU&t=96s
- https://www.youtube.com/watch?v=wWX4Dc3yD3Y
