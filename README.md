# hello-world

Random stuff goes here:

Ideas for qPCR project:

    With Selection.Validation
        .Delete
        .Add Type:=xlValidateInputOnly, AlertStyle:=xlValidAlertStop, Operator:=xlBetween
        .IgnoreBlank = True
        .InCellDropdown = True
        .InputTitle = "Hi"
        .ErrorTitle = "Error"
        .InputMessage = "" & Chr(10) & "Hi! Message 1."
        .ErrorMessage = "Error message!"
        .ShowInput = True
        .ShowError = True
    End With
