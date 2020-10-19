$(document).ready(function(){
	var form = $('#form_buying_product');

	

	$( ".hidden1" ).hide();
	$( ".hidden2" ).hide();
	$( ".hidden3" ).hide();

	$( ".hidden" ).hide();
	$( ".col_type_hidden" ).hide();
	$( 'input[name="rp"]' ).hide();
	$( 'select[name="quantity"]' ).hide();

	var i;
	i = 0.0;

    $(function() {
	  $('input[name="color"]').on('change', function(){
	    var value = $(this).val();
	    console.log(value);

	    //var disp = $( this ).css( "display" );
	    
	    if (value == '1 цвет'){
			$( "div.hidden1" ).css( "display", "block");
			$( "div.hidden2" ).css( "display", "none");
			$( "div.hidden3" ).css( "display", "none");
		}else if (value == '2 цвета'){
			$( "div.hidden2" ).css( "display", "block");
			$( "div.hidden1" ).css( "display", "block");
			$( "div.hidden3" ).css( "display", "none");
		}else if (value == '3 цвета'){
			i =+ 100.0
			$( "div.hidden3" ).css( "display", "block");
			$( "div.hidden1" ).css( "display", "block");
			$( "div.hidden2" ).css( "display", "block");
		};
		
	    
	  });
	});



	$(function() {
	  $('#id_rouse').on('change', function(){
	    var value = $(this).val();
	    
	    if (value == '101 роза'){
			i = 4790.0;
		}else if (value == '37 роз'){
			i = 2190.0;
		}else if (value == '41 роза') {
			i = 2390.0;
		}else if (value == '61 роза'){
			i = 3190.0;
		}else if (value == '51 роза'){
			i = 2790.0;
		}else if (value == '77 роз'){
			i = 3890.0;
		}else if (value == '19 роз'){
			i = 1190.0;
		}else if (value == '27 роз'){
			i = 1690.0;
		}else{
			i = 0.0;
		};
	    $('.myprice').text(i);
	    $('input[name="rp"]').val(i);
	    //$('#id_rp').value= i
	    console.log(value);
	    console.log($('input[name="rp"]').val(i));
	  });
	});
	
	//console.log(u);


	//console.log($("#id_rouse").val());

	//console.log($("#id_rouse option:selected").text());

	

	
});






// <p id="result"></p>
// <select id="list">
//   <option value="1">Первое значение</option>
//   <option value="2">Второе значение</option>
//   <option value="3">Третье значение</option>
// </select>
// ...
// <script>
// $(function() {
//   $('#list').on('change', function(){
//     var value = $(this).val();
//     $('#result').text(value);
//   });
// });