function Read(){
    var name=document.getElementById("getname").value;
    console.log(name);
    var rollno=document.getElementById("getroll").value;
    console.log(rollno);
    var admissionnumber=document.getElementById("getad").value;
    console.log(admissionnumber);
    var age=document.getElementById("getage").value;
    console.log(age);
    var op=document.getElementById("d");
    var dist=op.options[op.selectedIndex].value;
    console.log(dist);

    if(age>=18)
    {
        console.log("noteligible");
    
    }
    else{console.log("e");}

}

function addition()
{
    var op=document.getElementById("operation");
    var operation=op.options[op.selectedIndex].value;
    console.log();
    var num1=document.getElementById("operant1").value;
    var num2=document.getElementById("operant2").value;

    var x=parseInt(num1);
    var y=parseInt(num2);
    if(op=="add")
    {
        var num3=x+y;
    }
    else if(op=="sub")
    {
        var num3=x-y;
    }
    else if(op=="mul")
    {
        var num3=x*y;
    }
    else{
        var num3=x-y;
    }

    var num3=x+y;
    console.log(num3);

}

function large()

    var num1=document.getElementById("getnum1").value;
    var num2=document.getElementById("getnum2").value;
    var num3=document.getElementById("getnum3").value;
    var res=document.getElementById("result") ; 
    
    var x=parseInt(num1);
    var y=parseInt(num2);
    var y=parseInt(num3);


    if(x>y)
    {
         
        if(x>z)
            {
      var res=x;
        }
        else{
           var res=z;
        }
    }
    else{
        if(y>z)
{
   var res=y;
}
else{
   var res=z;
}
    }