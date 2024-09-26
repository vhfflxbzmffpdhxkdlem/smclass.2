//jqery선언
let num =0;
let num2 = 0;
let count = 0
$(function(){
  $("#right").click(function(){
    //alert("우측버튼클릭")
    if(900<=num){
      alert("우측끝에 도달했습니다. 우측이동은 불가합니다.")
      return false
    }
    $("#box").stop
    num += 100;
    num2 +=360
    $("#box").animate({
      left:num,"rotate":num2+"deg"
      
    },1000)
  })
  $("#left").click(function(){
    //alert("좌측버튼클릭")
    if(0>=num){
      alert("왼쪽끝에 도달했습니다. 좌측이동은 불가합니다.")
      return false
    }
    $("#box").stop
    num -= 100;
    num2 -=360
    $("#box").animate({
      right:num,"rotate":num2+"deg"
    },1000)
  })




})//jqery