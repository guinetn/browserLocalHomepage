## IDisposable
To release unmanaged resources. The garbage collector automatically releases the memory allocated to a managed object when that object is no longer used. However, it is not possible to predict when garbage collection will occur. Furthermore, the garbage collector has no knowledge of unmanaged resources such as window handles, or open files and streams.

You can release your resources before the garbage collector frees the object
Even with this explicit control over resources, the finalizer becomes a safeguard to clean up resources if the call to the Dispose method fails.

Call Dispose() to explicitly release unmanaged resources in conjunction with the garbage collector.

```cs
class BaseClass : IDisposable
{
   // Flag: Has Dispose already been called?
   bool disposed = false;

   // Public implementation of Dispose pattern callable by consumers.
   public void Dispose()
   {
      Dispose(true);
      GC.SuppressFinalize(this);
   }

   // Protected implementation of Dispose pattern.
   protected virtual void Dispose(bool disposing)
   {
      if (disposed)
         return;

      if (disposing) {
         // Free any other managed objects here.
         //
      }

      // Free any unmanaged objects here.
      //
      disposed = true;
   }

   ~BaseClass()
   {
      Dispose(false);
   }
}
```

Subclasses should implement the disposable pattern as follows:
They must override Dispose(Boolean) and call the base class Dispose(Boolean) implementation.
They can provide a finalizer if needed. The finalizer must call Dispose(false).


https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1?view=net-5.0#examples
```cs
using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class App
{
    // Excercise the Iterator and show that it's more
    // performant.
    public static void Main()
    {
        TestStreamReaderEnumerable();
        Console.WriteLine("---");
        TestReadingFile();
    }

    public static void TestStreamReaderEnumerable()
    {
        // Check the memory before the iterator is used.
        long memoryBefore = GC.GetTotalMemory(true);
      IEnumerable<String> stringsFound;
        // Open a file with the StreamReaderEnumerable and check for a string.
      try {
         stringsFound =
               from line in new StreamReaderEnumerable(@"c:\temp\tempFile.txt")
               where line.Contains("string to search for")
               select line;
         Console.WriteLine("Found: " + stringsFound.Count());
      }
      catch (FileNotFoundException) {
         Console.WriteLine(@"This example requires a file named C:\temp\tempFile.txt.");
         return;
      }

        // Check the memory after the iterator and output it to the console.
        long memoryAfter = GC.GetTotalMemory(false);
        Console.WriteLine("Memory Used With Iterator = \t"
            + string.Format(((memoryAfter - memoryBefore) / 1000).ToString(), "n") + "kb");
    }

    public static void TestReadingFile()
    {
        long memoryBefore = GC.GetTotalMemory(true);
      StreamReader sr;
      try {
         sr = File.OpenText("c:\\temp\\tempFile.txt");
      }
      catch (FileNotFoundException) {
         Console.WriteLine(@"This example requires a file named C:\temp\tempFile.txt.");
         return;
      }

        // Add the file contents to a generic list of strings.
        List<string> fileContents = new List<string>();
        while (!sr.EndOfStream) {
            fileContents.Add(sr.ReadLine());
        }

        // Check for the string.
        var stringsFound =
            from line in fileContents
            where line.Contains("string to search for")
            select line;

        sr.Close();
        Console.WriteLine("Found: " + stringsFound.Count());

        // Check the memory after when the iterator is not used, and output it to the console.
        long memoryAfter = GC.GetTotalMemory(false);
        Console.WriteLine("Memory Used Without Iterator = \t" +
            string.Format(((memoryAfter - memoryBefore) / 1000).ToString(), "n") + "kb");
    }
}

// A custom class that implements IEnumerable(T). When you implement IEnumerable(T),
// you must also implement IEnumerable and IEnumerator(T).
public class StreamReaderEnumerable : IEnumerable<string>
{
    private string _filePath;
    public StreamReaderEnumerable(string filePath)
    {
        _filePath = filePath;
    }

    // Must implement GetEnumerator, which returns a new StreamReaderEnumerator.
    public IEnumerator<string> GetEnumerator()
    {
        return new StreamReaderEnumerator(_filePath);
    }

    // Must also implement IEnumerable.GetEnumerator, but implement as a private method.
    private IEnumerator GetEnumerator1()
    {
        return this.GetEnumerator();
    }
    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator1();
    }
}

// When you implement IEnumerable(T), you must also implement IEnumerator(T),
// which will walk through the contents of the file one line at a time.
// Implementing IEnumerator(T) requires that you implement IEnumerator and IDisposable.
public class StreamReaderEnumerator : IEnumerator<string>
{
    private StreamReader _sr;
    public StreamReaderEnumerator(string filePath)
    {
        _sr = new StreamReader(filePath);
    }

    private string _current;
    // Implement the IEnumerator(T).Current publicly, but implement
    // IEnumerator.Current, which is also required, privately.
    public string Current
    {

        get
        {
            if (_sr == null || _current == null)
            {
                throw new InvalidOperationException();
            }

            return _current;
        }
    }

    private object Current1
    {

        get { return this.Current; }
    }

    object IEnumerator.Current
    {
        get { return Current1; }
    }

    // Implement MoveNext and Reset, which are required by IEnumerator.
    public bool MoveNext()
    {
        _current = _sr.ReadLine();
        if (_current == null)
            return false;
        return true;
    }

    public void Reset()
    {
        _sr.DiscardBufferedData();
        _sr.BaseStream.Seek(0, SeekOrigin.Begin);
        _current = null;
    }

    // Implement IDisposable, which is also implemented by IEnumerator(T).
    private bool disposedValue = false;
    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this);
    }

    protected virtual void Dispose(bool disposing)
    {
        if (!this.disposedValue)
        {
            if (disposing)
            {
                // Dispose of managed resources.
            }
            _current = null;
            if (_sr != null) {
               _sr.Close();
               _sr.Dispose();
            }
        }

        this.disposedValue = true;
    }

     ~StreamReaderEnumerator()
    {
        Dispose(false);
    }
}
// This example displays output similar to the following:
//       Found: 2
//       Memory Used With Iterator =     33kb
//       ---
//       Found: 2
//       Memory Used Without Iterator =  206kb
```