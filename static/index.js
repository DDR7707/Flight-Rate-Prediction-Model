
var initial1=true;
var initial2=true;
var initial3=true;
var initial4=true;
var place1="";
var place2="";
var packages=[];
var airStop=[];


$("#sourcePlace").click(function() {

  $(this).click(function() {
    if(!initial1){
       $("#destinationPlace option[value="+place1+"]").show();
    }
    place1=$("#sourcePlace :selected").val();
    $("#destinationPlace option[value="+place1+"]").hide();
    initial1=false;
  });
});

$("#destinationPlace").click(function() {

  $(this).click(function() {
    if(!initial2){
       $("#sourcePlace option[value="+place2+"]").show();
    }
    place2=$("#destinationPlace :selected").val();
    $("#sourcePlace option[value="+place2+"]").hide();
    initial2=false;
  });
});

$("#stops").click(function(){
  $(this).click(function(){
    if(!initial3){
      $("#addPackage option[value=1LL]").show();
      $("#addPackage option[value=1SL]").show();
      $("#addPackage option[value=2LL]").show();
      $("#addPackage option[value=changeAirports]").show();
    }
    var option=$("#stops :selected").val();
    if(option=="0"){
      packages=["One Long Layover","One Short Layover","Two Long Layover","Change Airports"];
      for(i=0;i<4;i++)
      $("#addPackage option[value="+packages[i]+"]").hide();
      initial3=false;
    }
    if (option=="1") {
      packages=["Two Long Layover"];
      $("#addPackage option[value="+packages[0]+"]").hide();
      initial3=false;
    }
    if (option=="2") {
      packages=["One Long Layover","One Short Layover"];
      $("#addPackage option[value="+packages[0]+"]").hide();
      $("#addPackage option[value="+packages[1]+"]").hide();
      initial3=false;
    }
    if (option=="4") {
      packages=["One Long Layover","One Short Layover","Two Long Layover"];
      $("#addPackage option[value="+packages[0]+"]").hide();
      $("#addPackage option[value="+packages[1]+"]").hide();
      $("#addPackage option[value="+packages[2]+"]").hide();
      initial3=false;
    }
    if(option=="3") {
      packages=["One Long Layover","One Short Layover","Two Long Layover"];
      $("#addPackage option[value="+packages[0]+"]").hide();
      $("#addPackage option[value="+packages[1]+"]").hide();
      $("#addPackage option[value="+packages[2]+"]").hide();
      initial3=false;
    }

  });
});


$("#addPackage").click(function(){
  $(this).click(function(){
    if(!initial4){
      $("#stops option[value=0]").show();
      $("#stops option[value=1]").show();
      $("#stops option[value=2]").show();
      $("#stops option[value=3]").show();
      $("#stops option[value=4]").show();
    }

    var option1=$("#addPackage :selected").val();
    if(option1==="One Long Layover"){
      airStop=["0","2","3","4"];
      $("#stops option[value="+airStop[0]+"]").hide();
      $("#stops option[value="+airStop[1]+"]").hide();
      $("#stops option[value="+airStop[2]+"]").hide();
      $("#stops option[value="+airStop[3]+"]").hide();
      initial4=false;
    }
    if(option1==="One Short Layover"){
      airStop=["0","2","3","4"];
      $("#stops option[value="+airStop[0]+"]").hide();
      $("#stops option[value="+airStop[1]+"]").hide();
      $("#stops option[value="+airStop[2]+"]").hide();
      $("#stops option[value="+airStop[3]+"]").hide();
      initial4=false;
    }
    if(option1==="Two Long Layover"){
      airStop=["0","1","3","4"];
      $("#stops option[value="+airStop[0]+"]").hide();
      $("#stops option[value="+airStop[1]+"]").hide();
      $("#stops option[value="+airStop[2]+"]").hide();
      $("#stops option[value="+airStop[3]+"]").hide();
      initial4=false;
    }
    if(option1==="Change Airports"){
      airStop=["0"];
      $("#stops option[value="+airStop[0]+"]").hide();
      initial4=false;
    }
  });
});
