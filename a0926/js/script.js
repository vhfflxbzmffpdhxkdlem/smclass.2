//1. ajax데이터 가져오기
let count=1;    //전역변수
let total = 0;  //전역변수
let avg = 0     //전역변수
let id_num;     //전역변수
let tr_this;
let temp = 0 

//jquery선언
$(function(){
  //ajax선언
  $.ajax({
    url:"js/stuData.json",
    type:"get",
    data:"",
    dataType:"json",
    success:function(data){
      let h_data = ""
      for(var i=0;i<data.length;i++){
          count++
          console.log("count : "+count)
          let total=(data[i].kor) + (data[i].eng) + (data[i].math)
          let avg= (total/3).toFixed(2)
          h_data += `<tr id=${data[i].no}>`
          h_data += `<td>${data[i].no}</td>`
          h_data += `<td>${data[i].name}</td>`
          h_data += `<td>${data[i].kor}</td>`
          h_data += `<td>${data[i].eng}</td>`
          h_data += `<td>${data[i].math}</td>`
          h_data += `<td>${total}</td>`
          h_data += `<td>${avg}</td>`
          h_data += `<td><button class="updateBtn">수정</button>
                         <button class="delBtn">삭제</button></td>`
          h_data += `</tr>`
        }
        $("#tbody").html(h_data)
      
      //입력버튼 이벤트
        $(document).on("click","#create",function(){
          //입력된 데이터 가져오기
          let name = $("#name").val()
          let kor = Number($("#kor").val())
          let eng = Number($("#eng").val())
          let math = Number($("#math").val())
          total = kor+eng+math
          avg = (total/3).toFixed(2)
          //입력된 데이터가 있는지 확인
          if($("#name").val().length<1||$("#kor").val().length<1||$("#eng").val().length<1||$("#math").val().length<1){
            alert("데이터를 입력하셔야 저장이 가능합니다.")
            return false
          }
          alert("학생성적을 입력합니다.")
          //표를 만들어서 추가시켜줌
          let h_data = ""
          h_data += `<tr id=${count}>`
          h_data += `<td>${count}</td>`
          h_data += `<td>${name}</td>`
          h_data += `<td>${kor}</td>`
          h_data += `<td>${eng}</td>`
          h_data += `<td>${math}</td>`
          h_data += `<td>${total}</td>`
          h_data += `<td>${avg}</td>`
          h_data += `<td><button class="updateBtn">수정</button>
                         <button class="delBtn">삭제</button></td>`
          h_data += `</tr>`
          $("#tbody").prepend(h_data)
          $("#name").val("")
          $("#kor").val("")
          $("#eng").val("")
          $("#math").val("")
          count++
        })
      //수정버튼 이벤트
        $(document).on("click",".updateBtn",function(){
          //수정버튼 클릭이 되어 있는지 확인
          if (temp==1){
            alert("수정완료 또는 수정 취소 버튼을 먼저 클리하셔야 합니다.")
            return false
          }
          $(this).css({"color":"red","font-weight":"600"})
          tr_this = $(this)
          alert("수정을 진행합니다.")
          $("create,update,updateCancel").toggle()
          //데이터 가져오기
          id_num = $(this).closest("tr").attr("id")
          console.log("id : "+id_num)
          let u_data = $(this).closest("tr");
          console.log(u_data.children("td:eq(1)").text());
          console.log(u_data.children("td:eq(2)").text());
          console.log(u_data.children("td:eq(3)").text());
          console.log(u_data.children("td:eq(4)").text());
          //입력창에 값넣기
          $("#name").val(u_data.children("td:eq(1)").text())
          $("#kor").val(u_data.children("td:eq(2)").text())
          $("#eng").val(u_data.children("td:eq(3)").text())
          $("#math").val(u_data.children("td:eq(4)").text())

        })


      //수정완료 이벤트

      //입력된 데이터가 있는지 확인

      //표를 만들어 수정해서 넣기

      //표를 만들어 추가시켜줌

      //데이터 지우기

      //수정 취소 이벤트

      //데이터 지우기

      //삭제버튼 이벤트
        $(document).on("click",".delBtn",function(){
          id_num = $(this).parent().parent().attr("id")
          if(confirm(id_num+"번학생 성적을 삭제하시겠습니까?")){
            $("#"+id_num).remove()
          }
        })

    },
  error:function(){
    alert("실패");
  }
})//ajax


})//jquery