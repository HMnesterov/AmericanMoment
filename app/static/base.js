$("button").click(function () {
    var imgUrl = $(this).data('rel');
    $("#area").html("<img src='" + imgUrl + "' alt='description' />");
});