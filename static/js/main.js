//Jeff sir code starts----------------------------------------------------------------------------+
var index = 0,
    slideIndex = 1;
var commentaryContext = {
    overid: 14,
    over: [{
        id: 1,
        ball: 14.5,
        runs: 4,
        batsman: 'Sachin',
        bowler: 'Bretlee',
        commentary: 'width on offer and it keeps low but Sachin manages to cut it away square of the wicket to the boundary'
    }, {
        id: 1,
        ball: 14.5,
        runs: 4,
        batsman: 'Sachin',
        bowler: 'Bretlee',
        commentary: 'width on offer and it keeps low but Sachin manages to cut it away square of the wicket to the boundary'
    }, {
        id: 1,
        ball: 14.5,
        runs: 4,
        batsman: 'Sachin',
        bowler: 'Bretlee',
        commentary: 'width on offer and it keeps low but Sachin manages to cut it away square of the wicket to the boundary'
    }, {
        id: 1,
        ball: 14.5,
        runs: 4,
        batsman: 'Sachin',
        bowler: 'Bretlee',
        commentary: 'width on offer and it keeps low but Sachin manages to cut it away square of the wicket to the boundary'
    }, {
        id: 1,
        ball: 14.5,
        runs: 4,
        batsman: 'Sachin',
        bowler: 'Bretlee',
        commentary: 'width on offer and it keeps low but Sachin manages to cut it away square of the wicket to the boundary'
    }, {
        id: 1,
        ball: 14.5,
        runs: 4,
        batsman: 'Sachin',
        bowler: 'Bretlee',
        commentary: 'width on offer and it keeps low but Sachin manages to cut it away square of the wicket to the boundary'
    }],
    endofover: {
        'over': 15,
        'runs': 24,
        'total': '157/3',
        'target': '400',
        'runrate': 7.53,
        'strike': {
            batsman: 'Sachin',
            runs: 100,
            balls: 79,
            bowler: 'Bret Lee',
            stats: '10-2-37-3',
            extras: '2wd'
        },
        'non_strike': {
            batsman: 'Dravid',
            runs: 100,
            balls: 79,
            bowler: 'Gillespie',
            stats: '10-2-37-3',
            extras: '2wd'
        }
    }
}
var sliderContext = {
    slider: [{
        id: 1,
        imageUrl: 'slider_image1.jpg',
        text: 'Ajinkya Rahane celebrates getting to 150, India v New Zealand, 3rd Test, Indore, 2nd day, October 9, 2016'
    }, {
        id: 2,
        imageUrl: 'slider_image2.jpg',
        text: 'Tim Paine celebrates the winning wicket, New South Wales v Tasmania, Matador Cup, Hurstville Oval, Sydney'
    }, {
        id: 3,
        imageUrl: 'slider_image3.jpg',
        text: 'Virat Kohli and Ajinkya Rahane added 365 for the fourth wicket, India\'s fifth-highest partnership in Tests, in Indore'
    }, {
        id: 4,
        imageUrl: 'slider_image4.jpg',
        text: 'David Warner was bowled for 6, South Africa v Australia, 4th ODI, Port Elizabeth, October 9, 2016 '
    }, {
        id: 5,
        imageUrl: 'slider_image5.jpg',
        text: 'Kyle Abbott finished with 4 for 40, South Africa v Australia, 4th ODI, Port Elizabeth, October 9, 2016'
    }]
}
var trendingContext = {
    trending: [{
        id: 1,
        imageUrl: 'article_image1.jpg',
        header: 'Black Caps under pressure',
        content: 'I am a very simple card. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'
    }, {
        id: 2,
        imageUrl: 'article_image2.jpg',
        header: 'Pakistan takes on Windies',
        content: 'I am a very simple card. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'
    }, {
        id: 3,
        imageUrl: 'article_image4.jpg',
        header: 'Hope is up for Bangladesh',
        content: 'I am a very simple card. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'
    }, {
        id: 4,
        imageUrl: 'article_image5.jpg',
        header: 'Australia strikes Sri Lanka',
        content: 'I am a very simple card. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.'
    }]
}
var livenewsContext = {
    livenews: [{
        id: 1,
        content: 'Pakistan make inroads to leave West Indies in trouble'
    }, {
        id: 2,
        content: 'Bangladesh let down by lack of Tests'
    }, {
        id: 3,
        content: 'Nobody expected us to play in this manner: Mushfiqur Rahim'
    }, {
        id: 4,
        content: 'Brathwaite\'s 50 provides West Indies healthy start'
    }, {
        id: 5,
        content: 'Raina ruled out; India retain same squad for last two ODIs'
    }, {
        id: 6,
        content: 'Stokes balances our side and gives options: Cook'
    }, {
        id: 7,
        content: 'Ranji Trophy 2016-17, Round 3: Top performers'
    }, {
        id: 8,
        content: 'Azhar Ali, Asad Shafiq take Pakistan\'s lead past 450'
    }, {
        id: 9,
        content: 'Derbyshire rope in Imran Tahir for 2017 season'
    }, {
        id: 10,
        content: 'England\'s narrowest win outside Ashes'
    }]
}
var scoreContext = {
    section: [{
        sectionName: 'Completed Matches',
        sectionIcon: 'done_all',
        matches: [{
            matchId: 1,
            matchLink: 'scorecard.html',
            scoreText: 'South Africa 415 &amp; 181/5 (44 ov) v CA XI 103 Match drawn'
        }]
    }, {
        sectionName: 'Live Matches',
        sectionIcon: 'whatshot',
        matches: [{
            matchId: 1,
            matchLink: 'scorecard.html',
            scoreText: 'New Zealand 285 v India 159/2 (30/50 ov)'
        }, {
            matchId: 1,
            matchLink: 'scorecard.html',
            scoreText: 'Australia 334 v Sri Lanka 259/2 (37/50 ov)'
        }, {
            matchId: 1,
            matchLink: 'scorecard.html',
            scoreText: 'England 240 v Bangladesh 228/7 (49/50 ov)'
        }]
    }, {
        sectionName: 'Upcoming Matches',
        sectionIcon: 'trending_up',
        matches: [{
            matchId: 1,
            matchLink: 'scorecard.html',
            scoreText: '4th ODI: India v New Zealand at Ranchi  -- Oct 26, 2016 (13:30 local | 08:00 GMT)'
        }, {
            matchId: 1,
            matchLink: 'scorecard.html',
            scoreText: '7th ODI: SA Women v NZ Women at Paarl -- Oct 24, 2016 (10:00 local | 08:00 GMT | 13:30 IST)'
        }]
    }]
}

function getContext() {
    var context1 = {
        overs: []
    };
    for (i = 0; i < 20; i++) {
        context1.overs.push(Object.assign({}, commentaryContext));
    }
    context1.postmatch = 'post-match';

    return context1;
}

function plusDivs(n) {
    showDivs(slideIndex += n);
}

function currentDiv(n) {
    showDivs(slideIndex = n);
}

function startSlideshow() {
    showDivs(slideIndex);
    setInterval(showSlides, 5000);
}

function showSlides() {
    showDivs(slideIndex += 1);
}

function showDivs(n) {
    var i;
    var x = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    if (x.length && dots.length) {
        if (n > x.length) { slideIndex = 1 }
        if (n < 1) { slideIndex = x.length }
        for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" w3-white", "");
        }
        x[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].className += " w3-white";
    }
}
$(document).ready(function() {
    try {
        $('.collapsible').collapsible({ accordion: false });

        var sliderHtml = Handlebars.templates.slider(sliderContext);
        $('#slider_container').html(sliderHtml);
        startSlideshow();

        var matchscoresHtml = Handlebars.templates.matchscores(scoreContext);
        $('#scores_list').html(matchscoresHtml);

        var liveNewsHtml = Handlebars.templates.livenews(livenewsContext);
        $('#live_news_section').html(liveNewsHtml);
        var trendingHtml = Handlebars.templates.trending(trendingContext);
        $('#article_container').html(trendingHtml);
        var commentHtml = Handlebars.templates.overs(getContext());
        $('#full_commentary').html(commentHtml);
    } catch (error) {}
});
//Jeff sir code ends----------------------------------------------------------------------------+


//Ashvath code starts----------------------------------------------------------------------------+

//instantiate all material components 
$(document).ready(function() {
    $('ul.tabs').tabs();
    $('.modal').modal();
    $('select').formSelect();
    M.Chips.init($('.cchips'), { placeholder: "Add more", });
    $('input.autocomplete').autocomplete({
        data: {
            "Apple": null,
            "Aple": null,
            "Ape": null,
            "Ap": null,
            "Apaaale": null,
            "Appleaa": null,
            "Microsoft": null,
            "Google": 'https://placehold.it/250x250'
        },
    });
});

//adding chips(teams or players) from select option
function addTeam(obj) {
    var instance = M.Chips.getInstance(obj.parentElement.parentElement.children[5]);

    instance.addChip({
        'tag': obj.value
    })
}

function addformat(obj) {
    var instance = M.Chips.getInstance(obj.parentElement.parentElement.children[5]);
    instance.addChip({
        'tag': obj.value
    })
}



//submitting create and edit modals for teams and tournaments
function submitForm(form, type, teamortour) {
    var instance = M.Chips.getInstance(form.children[0].children[5]);
    var allteams = [];
    instance.chipsData.forEach(element => {
        allteams.push(element.tag);
    });
    allteams = allteams.join(",");
    var data = teamortour == 0 ? {
        tname: form.tname.value,
        place: form.place.value,
        year: form.year.value,
        allteams: allteams,
        win: form.win.value,
        loss: form.loss.value,
        draw: form.draw.value,
    } : {
        name: form.name.value,
        type: form.type.value,
        allteams: allteams,
        tour: form.t.value,
    }
    if (type == 2)var data= {
        id : form.id.value,
        tname: form.tname.value,
        place: form.place.value,
        year: form.year.value,
        allteams: allteams,
        win: form.win.value,
        loss: form.loss.value,
        draw: form.draw.value,
    }
    $.ajax({
        type: "POST",
        url: teamortour == 0 ? '/tournament/create' : '/team/create',
        data: data,
        success: function(res) {}
    });
}

//for creating match
function createMatch(formdata) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/match/create",
        data: {
            status: formdata['status'].value,
            Winner: formdata['Winner'].value,
            Loser: formdata['Loser'].value,
            Type: formdata['Type'].value,
            Time: formdata['Time'].value,
            id: formdata['id'].value,
            fromcreate: formdata['fromcreate'].value,
            Date: formdata['Date'].value,
            Venue: formdata['Venue'].value,
            user: formdata['user'].value,
        },
        success: function(data) {

        }
    });
}

//copy match code function
function CopyToClipboard(id) {
    var r = document.createRange();
    r.selectNode(document.getElementById(id));
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(r);
    document.execCommand('copy');
    window.getSelection().removeAllRanges();
    window.location.reload(true);
}

//for submitting comments without page reload
function submitComment(formdata) {
    event.preventDefault();
    var others = [];
    formdata['others[]'].forEach(element => {
        if (element.checked) {
            others.push(element.defaultValue);
        }
    })
    if (formdata["wicket"].value !== "" || formdata["wicket"].value == " ") {
        others.push(formdata["wicket"].value);
    }
    formdata["ball"].value = formdata["run"].value + 1
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/match/event",
        data: {
            inning: formdata['inning'].value,
            over: formdata['over'].value,
            run: formdata['run'].value,
            ball: formdata['ball'].value,
            striker: formdata['batsman1'].value,
            nonstriker: formdata['batsman2'].value,
            bowler: formdata['bowler'].value,
            others: others.join(','),
            remark: formdata['remark'].value,
        },
        success: function(data) {
            M.toast({ html: document.getElementsByClassName("successtoast")[0].innerHTML, classes: 'rounded', displayLength: '2000' });
            if ($("#recentcomm").children().length == 6) {
                $("#recentcomm").children().last().remove();
            }
            var other = '';
            data.recentcomment = data.recentcomment[0];
            if (data.recentcomment.others != null && (data.recentcomment.others).split(',')[1] != "") {
                for (var i = 1; i < (data.recentcomment.others).split(',').length; i++) {
                    other += "<span class='pill'>" + (data.recentcomment.others).split(',')[i] + "</span>";
                }
            }
            $("#recentcomm").prepend("<li class='collection-item avatar'><i style='margin-top:10px;' class='circle' run=" + data.recentcomment.run + ">" + data.recentcomment.over + "." + data.recentcomment.ball + "</i><span style='margin-top:13px;margin-bottom:5px;' class='title'><span style='background-color:lightblue;border-radius:80%;padding:7px 10px;'>" + data.recentcomment.run + "</span> <b>" + data.recentcomment.bowler + "</b> to <b>" + data.recentcomment.batsman + "</b>" + other + "</span><p style='margin-left:4px'>" + data.recentcomment.remark + "</p></li>");
            circleColor();
        },
        error: function() {
            M.toast({ html: document.getElementsByClassName("failtoast")[0].innerHTML, classes: 'rounded', displayLength: '8000' });
        }
    });
}

//initializing edit modals
function initTeams(id) {
    const tempteams = $("." + id + "chips")[0];
    var data = [];
    if ($("#" + id + "allteams").val() != "") {
        $("#" + id + "allteams").val().split(',').forEach(element => {
            data.push({ tag: element });
        });
    }
    console.log(data)
    M.Chips.init(
        tempteams, {
            placeholder: "Add more",
            data: data,
        }
    );
    var instance = M.Chips.getInstance(tempteams);
}
//initializing comment edit modals
function initComments(comment){
    $("#cid").val(comment.id);
    $("#mid").val(comment.match_id);
    $("#bat").val(comment.batsman.toLowerCase());
    $("#bowl").val(comment.bowler.toLowerCase());
    $("#non").val(comment.nonstriker.toLowerCase());
    $("#einning"+comment.inning).click();
    eclearplayers();
    $("#erun"+comment.run).click();
    $("#eover").val(comment.over);
    $("#eball"+comment.ball).click();
    setOthers();
    comment.others.split(",").forEach(element => {
        $("#e"+element.replace(/\s/g, "").toLowerCase()).click();
      if(!["Wide","No Ball","Byes","Leg Byes"].includes(element)){
        $("#ewicket").val(element);
      }
    });
    $("#eremark").val(comment.remark);  
  }

function swap(type) {
    if (type == 1 && (document.getElementsByName("inning")[0].checked || document.getElementsByName("inning")[1].checked)) {
        stk = $("#body > div > div > div.center > div > div.center-pane > div > div > form > div:nth-child(6) > input");
        nstk = $("#body > div > div > div.center > div > div.center-pane > div > div > form > div:nth-child(10) > input");
        temp = stk.val();
        stk.val(nstk.val()).change();
        nstk.val(temp).change();
    }
    if (type == 2 && (document.getElementsByName("einning")[0].checked || document.getElementsByName("einning")[1].checked)) {
        stk = $("#edit > form > div.modal-content > div:nth-child(12) > input");
        nstk = $("#edit > form > div.modal-content > div:nth-child(16) > input");
        temp = stk.val();
        stk.val(nstk.val()).change();
        nstk.val(temp).change();
    }
}

function setOthers() {
    if ($("#ewide").prop("checked")) $("#ewide").click();
    if ($("#enoball").prop("checked")) $("#enoball").click();
    if ($("#ebyes").prop("checked")) $("#ebyes").click();
    if ($("#elegbyes").prop("checked")) $("#elegbyes").click();
}

//login page toggle
$("#login-as-commentator").click(() => {
    $("#login-tab").html("<a class='white-text active'>commentator login</a>");
    $("#organiser-login").hide();
    $("#commentator-login").show();
});
$("#login-as-organiser").click(() => {
    $("#login-tab").html("<a class='white-text active'>organiser login</a>");
    $("#commentator-login").hide();
    $("#organiser-login").show();
});


// update players after getting innings in real time
$('input[type=radio][name=inning]').change(clearplayers);

function clearplayers() {
    document.getElementsByName("batsman1")[0].innerHTML = "<option disabled>Choose Striker</option>";
    document.getElementsByName("batsman2")[0].innerHTML = "<option disabled>Choose Non-striker</option>";
    document.getElementsByName("bowler")[0].innerHTML = "<option disabled>Choose Bowler</option>";
    if (document.getElementsByName("batsman1")[0].innerHTML.length < 70) {
        var inn = document.getElementsByName("inning")[0].checked ? 1 : 2,
            t1 = "",
            t2 = "";
        $.ajax({
            type: "POST",
            url: '/fetch/' + inn,
            success: function(data) {
                for (var i = 0; i < data.bat.length; i++) {
                    t1 += "<option value=" + data.bat[i] + ">" + data.bat[i] + "</option>";
                    t2 += "<option value=" + data.bowl[i] + ">" + data.bowl[i] + "</option>";
                    t3 = data.bat[1];
                }
                document.getElementsByName("batsman1")[0].innerHTML += t1;
                document.getElementsByName("batsman2")[0].innerHTML += t1;
                document.getElementsByName("bowler")[0].innerHTML += t2;
                document.getElementsByName("batsman2")[0].value = t3;
                $('select').formSelect();
            }
        });
    }
}
$('input[type=radio][name=einning]').change(eclearplayers);

function eclearplayers() {
    document.getElementsByName("ebatsman1")[0].innerHTML = "<option disabled>Choose Striker</option>";
    document.getElementsByName("ebatsman2")[0].innerHTML = "<option disabled>Choose Non-striker</option>";
    document.getElementsByName("ebowler")[0].innerHTML = "<option disabled>Choose Bowler</option>";
    if (document.getElementsByName("ebatsman1")[0].innerHTML.length < 70) {
        var inn = document.getElementsByName("einning")[0].checked ? 1 : 2,
            t1 = "",
            t2 = "",
            t3;
        $.ajax({
            type: "POST",
            url: '/fetch/' + inn,
            success: function(data) {
                for (var i = 0; i < data.bat.length; i++) {
                    t1 += "<option value=" + data.bat[i] + ">" + data.bat[i] + "</option>";
                    t3 += "<option value=" + data.bat[2] + ">" + data.bat[2] + "</option>";
                    t2 += "<option value=" + data.bowl[i] + ">" + data.bowl[i] + "</option>";
                }
                document.getElementsByName("ebatsman1")[0].innerHTML += t1;
                document.getElementsByName("ebatsman2")[0].innerHTML += t1;
                document.getElementsByName("ebowler")[0].innerHTML += t2;
                document.getElementsByName("ebatsman2")[0].value = t3;
                $('select').formSelect();
                $("#edit > form > div.modal-content > div:nth-child(18) > input").val(capitalize($("#bowl").val())).change();
                $("#edit > form > div.modal-content > div:nth-child(12) > input").val(capitalize($("#bat").val())).change();
                $("#edit > form > div.modal-content > div:nth-child(16) > input").val(capitalize($("#non").val())).change();
            }
        });
    }
}

//for real time scorecard updating
//to hide second inning until first inning is over
function show() {
    if ($("#inning1").children().length > 0) {
        $('#show1').css("display", "block");
        $('#show11').css("display", "block");
        $('#show111').css("display", "block");
        $('#show2222').css("display", "block");
    }

    if ($("#inning2").children().length > 0) {
        $('#show2').css("display", "block");
        $('#show22').css("display", "block");
        $('#show222').css("display", "block");
        $('#show2222').css("display", "block");
    }
}

//set appropraite circle color in commentary according to runs scored
function circleColor() {
    for (var i = 0; i < document.getElementsByClassName('circle').length; i++) {
        if (document.getElementsByClassName('circle')[i].getAttribute("run") == '4' || document.getElementsByClassName('circle')[i].getAttribute("run") == '6') {
            document.getElementsByClassName('circle')[i].style.backgroundColor = "green";
        } else {
            document.getElementsByClassName('circle')[i].style.backgroundColor = "#0d67de";
        }
    }
    for (var i = 0; i < document.getElementsByClassName('pill').length; i++) {
        if (!["No Ball", "Wide", "Byes", "Leg Byes"].includes(document.getElementsByClassName('pill')[i].textContent)) {
            var x = document.getElementsByClassName('pill')[i].parentElement.parentElement;
            x.children[0].style.backgroundColor = "red";
        }
    }
}

//updating match live
function live() {
    var x='',y='';
    $.ajax({
      type:"GET",
      url:'live/'+$("#match").val(),
      success: function(data){
        for(var i=0;i<data.bowlive.length;i++){
          extras=parseInt(data.bowlive[i].no_balls)+parseInt(data.bowlive[i].wides);
          x+="<tr id='bowlive"+data.bowlive[i].id+"'><td>"+data.bowlive[i].name[0].toUpperCase()+data.bowlive[i].name.slice(1)+"</td><td></td><td>"+data.bowlive[i].overs+"</td><td>"+data.bowlive[i].maidens+"</td><td>"+data.bowlive[i].runs+"</td><td>"+data.bowlive[i].wickets+"</td><td>"+extras+"</td><td>"+data.bowlive[i].economy+"</td></tr>";
        }
  
        $("#bowlive").html(x);
        y+="<tr id='batlive"+data.batlive[0].id+"'><td>"+data.batlive[0].name[0].toUpperCase()+data.batlive[0].name.slice(1)+"</td><td>"+data.batlive[0].status+"</td><td>"+data.batlive[0].runs+"</td><td>"+data.batlive[0].balls+"</td><td>"+data.batlive[0].fours+"</td><td>"+data.batlive[0].sixes+"</td><td>"+data.batlive[0].strike_rate+"</td></tr>";
        y+="<tr id='batlive"+data.batlive[1].id+"'><td>"+data.batlive[1].name[0].toUpperCase()+data.batlive[1].name.slice(1)+"</td><td>"+data.batlive[1].status+"</td><td>"+data.batlive[1].runs+"</td><td>"+data.batlive[1].balls+"</td><td>"+data.batlive[1].fours+"</td><td>"+data.batlive[1].sixes+"</td><td>"+data.batlive[1].strike_rate+"</td></tr>";
        $("#batlive").html(y);
  
        if(data.last!=0)
        {
          $('#last').text("Last Wicket: "+data.last.name[0].toUpperCase()+data.last.name.slice(1)+" "+data.last.runs+"("+data.last.balls+")");
          $("#fow"+data.inni).html(data.fow);
        }else{
          $('#last').text("");
        }
  
        $('#partnership').text("Partnership: "+parseInt(data.batlive[1].runs+data.batlive[0].runs)+"("+parseInt(data.batlive[1].balls+data.batlive[0].balls)+")");
        $("#livehead").text(data.matchlive[0]+" "+data.matchlive[1]+"/"+data.matchlive[3]+" "+data.matchlive[2]+" Overs");
        if(document.getElementsByClassName(data.livecomment[0].id+"remark").length==1){
        if(data.change){
          $("#livecomm").empty();
        }
        if($("#livecomm").children().length==12){
        $("#livecomm").children().last().remove();
         }
        var other='';
        data.livecomment=data.livecomment[0];
        if(data.livecomment.others!=null && (data.livecomment.others).split(',')[1]!=""){
          for(var i=1;i<(data.livecomment.others).split(',').length;i++) {
            other+="<span class='pill'>"+(data.livecomment.others).split(',')[i]+"</span>";
          }
        }
        $("#livecomm").prepend("<li class='collection-item avatar'><i style='margin-top:10px;' class='circle "+data.livecomment.id+"color' run='"+data.livecomment.run+"'>"+data.livecomment.over+"."+data.livecomment.ball+"</i><span style='margin-top:13px;margin-bottom:5px;' class='title'><span style='background-color:lightblue;border-radius:80%;padding:7px 10px;' class='"+data.livecomment.id+"run'>"+data.livecomment.run+"</span> <b>"+data.livecomment.bowler+"</b> to <b>"+data.livecomment.batsman+"</b>"+other+"</span><p style='margin-left:4px' class='"+data.livecomment.id+"remark'>"+data.livecomment.remark+"</p></li>");
        circleColor();
      }
    }
    });
  }
  circleColor();
  show();
  //display match code after match creation
  document.addEventListener('DOMContentLoaded', function() {
    // #create a webSocketBridge object
    const webSocketBridge = new channels.WebSocketBridge();
    // #create connection with website
    webSocketBridge.connect('/ws/');
    webSocketBridge.listen(function(action, stream) {
      //listen for submit in website
  
      if(action.event == "UniqueID") {
        var instance1 = M.Modal.getInstance(document.getElementById('create'));
        var instance2 = M.Modal.getInstance( document.getElementById('displayUID'));
        instance1.close();
        instance2.open();
        document.getElementById('uidisphead').textContent="Match code for "+action.name+" of "+action.tname;
        document.getElementById('uidisp').innerHTML=action.uid;
      }
  
      if(action.event == "New Commentary" && $("#match").val()==action.id && $("#status").val()=="Live") {
        show();
        var other='';
        if(action.others!=null && (action.others).split(',')[1]!=""){
          for(var i=1;i<(action.others).split(',').length;i++) {
            other+="<span class='pill'>"+(action.others).split(',')[i]+"</span>";
          }
        }
          var card=$("<li class='collection-item avatar'><i style='margin-top:10px;' class='circle "+action.cid+"color' run='"+action.runs+"'>"+action.overs+"."+action.balls+"</i><span style='margin-top:13px;margin-bottom:5px;' class='title'><span style='background-color:lightblue;border-radius:80%;padding:7px 10px;' class='"+action.cid+"run'>"+action.runs+"</span> <b>"+action.bowler+"</b> to <b>"+action.batsman+"</b>"+other+"</span><p style='margin-left:4px' class='"+action.cid+"remark'>"+action.remarks+"</p></li>");
          $('#comm'+action.inning).append(card);
          circleColor();
      }
  
      if(action.event == "Edited Commentary" && $("#match").val()==action.id && $("#status").val()=="Live") {
        $("."+action.cid+"remark").text(action.remarks);
        $("."+action.cid+"run").text(action.runs);
        $("."+action.cid+"color").attr("run",action.runs);
        circleColor();
      }
  
      if(action.event == "Match" && $("#match").val()==action.id  ) {
      if(action.winner[4]==1){
        $("#first_score").text(action.winner[1]+"/"+action.winner[3]+" "+action.winner[2]);
        $("#second_score").text(action.loser[1]+"/"+action.loser[3]+" "+action.loser[2]);
      }
      else{
        $("#second_score").text(action.winner[1]+"/"+action.winner[3]+" "+action.winner[2]);
        $("#first_score").text(action.loser[1]+"/"+action.loser[3]+" "+action.loser[2]);
      }
      }
  
      if(action.event == "Batsman" && $("#match").val()==action.id) {
        if($("#bat"+action.thisid).length){
          $("#bat"+action.thisid).html("<td>"+action.name[0].toUpperCase()+action.name.slice(1)+"</td><td>"+action.status+"</td><td>"+action.runs+"</td><td>"+action.balls+"</td><td>"+action.fours+"</td><td>"+action.sixes+"</td><td>"+action.sr+"</td>");
        }
        else{
          var row=$("<tr id=bat"+action.thisid+"><td>"+action.name[0].toUpperCase()+action.name.slice(1)+"</td><td>"+action.status+"</td><td>"+action.runs+"</td><td>"+action.balls+"</td><td>"+action.fours+"</td><td>"+action.sixes+"</td><td>"+action.sr+"</td></tr>");
          $("#inning"+action.inning).append(row);
        }
      }
  
      if(action.event == "Bowler" && $("#match").val()==action.id) {
        live();
        if($("#bowl"+action.thisid).length){
          $("#bowl"+action.thisid).html("<td>"+action.name[0].toUpperCase()+action.name.slice(1)+"</td><td></td><td>"+action.overs+"</td><td>"+action.maidens+"</td><td>"+action.runs+"</td><td>"+action.wickets+"</td><td>"+action.extras+"</td><td>"+action.eco+"</td>");
        }
        else{
          var row=$("<tr id=bowl"+action.thisid+"><td>"+action.name[0].toUpperCase()+action.name.slice(1)+"</td><td></td><td>"+action.overs+"</td><td>"+action.maidens+"</td><td>"+action.runs+"</td><td>"+action.wickets+"</td><td>"+action.extras+"</td><td>"+action.eco+"</td></tr>");
          $("#inningbowl"+action.inning).append(row);
        }
      }
    })
    //object for debugging
    document.ws=webSocketBridge;
  });
//Ashvath code ends----------------------------------------------------------------------------+
// ---------Responsive-navbar-active-animation-----------
function test() {
    var tabsNewAnim = $('#navbarSupportedContent');
    var selectorNewAnim = $('#navbarSupportedContent').find('li').length;
    var activeItemNewAnim = tabsNewAnim.find('.active');
    var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
    var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
    var itemPosNewAnimTop = activeItemNewAnim.position();
    var itemPosNewAnimLeft = activeItemNewAnim.position();
    $(".hori-selector").css({
        "top": itemPosNewAnimTop.top + "px",
        "left": itemPosNewAnimLeft.left + "px",
        "height": activeWidthNewAnimHeight + "px",
        "width": activeWidthNewAnimWidth + "px"
    });
    $("#navbarSupportedContent").on("click", "li", function(e) {
        $('#navbarSupportedContent ul li').removeClass("active");
        $(this).addClass('active');
        var activeWidthNewAnimHeight = $(this).innerHeight();
        var activeWidthNewAnimWidth = $(this).innerWidth();
        var itemPosNewAnimTop = $(this).position();
        var itemPosNewAnimLeft = $(this).position();
        $(".hori-selector").css({
            "top": itemPosNewAnimTop.top + "px",
            "left": itemPosNewAnimLeft.left + "px",
            "height": activeWidthNewAnimHeight + "px",
            "width": activeWidthNewAnimWidth + "px"
        });
    });
}
$(document).ready(function() {
    setTimeout(function() { test(); });
});
$(window).on('resize', function() {
    setTimeout(function() { test(); }, 500);
});
$(".navbar-toggler").click(function() {
    $(".navbar-collapse").slideToggle(300);
    setTimeout(function() { test(); });
});



// --------------add active class-on another-page move----------
jQuery(document).ready(function($) {
    // Get current path and find target link
    var path = window.location.pathname.split("/").pop();

    // Account for home page with empty path
    if (path == '') {
        path = 'index.html';
    }

    var target = $('#navbarSupportedContent ul li a[href="' + path + '"]');
    // Add active class to target link
    target.parent().addClass('active');
});