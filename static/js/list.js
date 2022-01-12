function openNav(type) {
    document.getElementById(type).style.height = "100%";
  }
  
  $('#createsel').change(function(){
    var y=$('#createsel').val();
    var x=$('#cteams').val().split(",");
    if(x.indexOf(y)<0){
      document.getElementsByClassName("cteams")[0].style.display="block";
      box=document.getElementsByClassName("cteams")[0];
      box.children[0].children[0].children[0].innerHTML+="<td><div class='chip' value="+y+" type='cteams'>"+y+"<span class='closebtn' onclick='removechip(this.parentElement)'>&times</span></div></td>";
      if(x!=''){y=","+y}
      else{box.style.display="block"}
      document.getElementById("cteams").value+=y;
    }
  });
  
  function changesel(sel,id){
    var y=sel.value;
    let temp='eteams_'+id;
    var x=document.getElementById(temp).value.split(",");
    if(x.indexOf(y)<0){
      let temp="eteams "+id;
      document.getElementsByClassName(temp)[0].style.display="block";
      box=document.getElementsByClassName(temp)[0];
      box.children[0].children[0].children[0].innerHTML+="<td><div class='chip' value="+y+" type='eteams_"+id+"' >"+y+"<span class='closebtn' onclick='removechip(this.parentElement)'>&times</span></div></td>";
      if(x!=''){y=","+y}
      document.getElementById("eteams_"+id).value+=y;
    }
  }
  
  function closeNav(type) {
    document.getElementById(type).style.height = "0%";
  }
  
  function removechip(parent) {
    var team=parent.getAttribute("value");
    var type=parent.getAttribute("type");
    parent.style.display="none";
    var x=document.getElementById(type).value.split(",");
    x.splice(x.indexOf(team),1);
    document.getElementById(type).value=x.join(",");
    if(x==''){
      if(type.split('_')[0]=="eteams"){
      z="eteams "+type.split('_')[1]
    }
    else{
      z=type;
    }
      document.getElementsByClassName(z)[0].style.display="none";
    }
  }