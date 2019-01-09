# hello-world

Random stuff goes here:

Read links:
https://hackernoon.com/no-kaggle-is-unsuitable-to-study-ai-ml-a-reply-to-ben-hamner-27283878cede

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
