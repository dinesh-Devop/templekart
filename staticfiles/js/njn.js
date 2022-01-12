// mockda

var id=parseInt(document.getElementById('sid').value);

$.ajax({
  type:"GET",
  url:'/stats/'+id,
  
  headers: {
    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
  },
  async:false,
  success: function(context){
    //var instance = JSON.parse(context["matchesplayed"]);
    c=parseInt(context.matchdraw)
    
    
    a=parseInt(context.matcheswon)
    b=parseInt(context.matcheslost)
    d=parseInt(context.Firstbattingwon)
    e=parseInt(context.secondbattingwon)
    f=parseInt(context.last5mathchesrunsscored[0])
    g=parseInt(context.last5mathchesrunsscored[1])
    h=parseInt(context.last5mathchesrunsscored[2])
    i=parseInt(context.last5mathchesrunsscored[3])
    j=parseInt(context.last5mathchesrunsscored[4])
    k=context.last5matchdates[0]
    l=context.last5matchdates[1]
    m=context.last5matchdates[2]
    n=context.last5matchdates[3]
    o=context.last5matchdates[4]
    p=parseInt(context.last5matchesrunsconceeded[0])
    q=parseInt(context.last5matchesrunsconceeded[1])
    r=parseInt(context.last5matchesrunsconceeded[2])
    s=parseInt(context.last5matchesrunsconceeded[3])
    t=parseInt(context.last5matchesrunsconceeded[4])
    u=parseInt(context.last5matcheswicketstaken[0])
    v=parseInt(context.last5matcheswicketstaken[1])
    w=parseInt(context.last5matcheswicketstaken[2])
    xc=parseInt(context.last5matcheswicketstaken[3])
    xv=parseInt(context.last5matcheswicketstaken[4])
    df=parseInt(context.last5matcheswicketslost[0])
    vf=parseInt(context.last5matcheswicketslost[1])
    cf=parseInt(context.last5matcheswicketslost[2])
    bf=parseInt(context.last5matcheswicketslost[3])
    lf=parseInt(context.last5matcheswicketslost[4])
    


const runsScoredData = {
    datasets: [{
      label: 'Runs Scored',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [{ x: k, y: f}, { x: l, y: g }, { x: m, y: h }, { x: n, y: i }, { x: o, y: j }],
    }, {
      label: 'Runs Conceeded',
      backgroundColor: 'rgb(54, 162, 235)',
      borderColor: 'rgb(54, 162, 235)',
      data: [{ x: k, y: p}, { x: l, y: q }, { x: m, y: r }, { x: n, y: s}, { x: o, y: t }],
    }]
  };
  
  const wicketsTakenData = {
    datasets: [{
      label: 'Wickets Taken',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [{ x: k, y: u }, { x: l, y: v }, { x: m, y: w }, { x: n, y: xc }, { x: o, y: xv }],
    }, {
      label: 'Wickets Lost',
      backgroundColor: 'rgb(54, 162, 235)',
      borderColor: 'rgb(54, 162, 235)',
      data: [{ x: k, y: df }, { x: l, y: vf }, { x: m, y: cf }, { x: n, y: bf }, { x: o, y: lf }],
    }]
  };


    
      
   
  const winLossData = {
    
    labels: [
      'Wins',
      'Losses',
      'Draw'
    ],
    datasets: [{
      data: [a, b, c],
     
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'
      ],
      hoverOffset: 4
    }]
  }; 
  
  const winInningsData = {
    labels: [
      'Bat First',
      'Bat Second',
      'Draw'
    ],
    datasets: [{
      data: [d, e, c],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'
      ],
      hoverOffset: 4
    }]
  };;
  
  // functions
  
  const runsScoredEl = document.getElementById('runsScored');
  var runsScored = new Chart(runsScoredEl, {
    type: 'bar',
    data: runsScoredData
  });
  
  const wicketsTakenEl = document.getElementById('wicketsTaken');
  var wicketsTaken = new Chart(wicketsTakenEl, {
    type: 'bar',
    data: wicketsTakenData
  });
  
  const winLossEl = document.getElementById('winLoss');
  var winLoss = new Chart(winLossEl, {
    type: 'doughnut',
    data: winLossData
  });
  
  const winInningsEl = document.getElementById('winInnings');
  var winLoss = new Chart(winInnings, {
    type: 'doughnut',
    data: winInningsData
    
  });  }});