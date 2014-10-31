$(function() {
    $('.vote-button').click(function(){
        voteForPost($(this));
        return false;
    });

    if($.fn.ajaxForm) {
        $('form.ajax-form').ajaxForm({beforeSend: setCSRFToken, success: addPostCallback, dataType: 'json'});
    }
    $('.send-post-button').click(function(){
        if($('#rules').is(':checked'))
            $('#post-form').submit();
        else
            alert("Вы должны согласиться с правилами конкурса");
        return false;
    });
    
    //
    $('.btn-post-form-open').click(function(){
        $('.posting__before').hide();
        $('.posting__form').show();
        return false;
    });
});

function voteForPost(elem) {
    var url = elem.attr('data-url');
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        beforeSend: setCSRFToken,
        success: voteCallback
    });
    return false;
}

function voteCallback(responseText, statusText, xhr) {
    if(responseText.success==true) {
        var id = responseText.id;
        $('#vote-count-' + id).html(parseInt($('#vote-count-' + id).html())+1);
    } else {
        alert(responseText.html);
    }
}

function setCSRFToken(xhr, settings) {
    var csrftoken = $.cookie('csrftoken');
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
}

function addPostCallback(responseText, statusText, xhr, $form) {
    if(responseText.success==true) {
        $('.posting__form').hide();
        $('.posting__after').show();
    } else {
        alert(responseText.html);
    }
}