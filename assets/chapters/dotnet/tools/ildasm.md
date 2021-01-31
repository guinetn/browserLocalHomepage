# Ildasm - Microsoft Diassembler Tool

Tool to see the IL code

class Class1
{
    Protected override void Finalize()
    {
        try{..}
        finally { base.Finalize();}
    }
}

method family hidebysig virtual instance void
Finalize() cil managed
{
    // Code size 10 (0xa)
    .maxstack 1
    .try
    {
      IL_0000: leave.s IL_0009
    } // end .try
    finally
    {
        IL_0002: ldarg.0
        IL_0003: call instance void [mscorlib]System.Object::Finalize()
        IL_0008: endfinally
    } // end handler
    IL_0009: ret
} // end of method Class1::Finalize