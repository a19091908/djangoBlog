$('document').ready(function(){
	$('input[name="input_delete"]').on('click', function(){
		return confirm("確定刪除?");
	});
});