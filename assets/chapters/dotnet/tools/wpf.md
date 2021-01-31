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

https://github.com/dotnet/wpf
https://github.com/Microsoft/WPF-Samples

## start

```dos
dotnet new wpf -o MyWPFApp
cd MyWPFApp
dotnet run
```

### COMMANDS

Separate UI component (semantic) from the logic to execut on command invocation
You can test business logic separately using test cases and also your UI code is loosely coupled to business logic.

* ICommand 

```cs
event EventHandler CanExecuteChanged;    // invoked when changes occur that can change whether or not the command can be executed.
bool CanExecute(object parameter);       // whether the command can be executed or not
void Execute(object parameter);          // Runs the command logic
```

Bu it does not allow to have a different logic for CanExecute or Execute
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

<CheckBox Content="CheckBox"
          Command="{Binding YourCommand}"
          CommandParameter="{Binding IsChecked, RelativeSource={RelativeSource Self}}" />
          CommandParameter="{Binding IsChecked, RelativeSource={RelativeSource Self}, Mode=OneWay}

<CheckBox Content="{Binding Path=Name}"
          CommandParameter="{Binding}"
          Command="{Binding DataContext.AddRemovePresetAssignmentCommand,
          RelativeSource={RelativeSource FindAncestor,
                           AncestorType={x:Type UserControl}}}">
                    
MVVM

XAML's namespaces:
xmlns:t="http://schemas.telerik.com/2008/xaml/presentation" 
xmlns:i="http://schemas.microsoft.com/expression/2010/interactivity"          Add System.Windows.Interactivity in project references

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

implement INotifyPropertyChanged on the ViewModel 

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

```
```

https://docs.microsoft.com/en-gb/dotnet/api/system.windows.input.routedcommand?view=net-5.0

#### 
```
```
