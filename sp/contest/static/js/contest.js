$(function() {
    $(document).on('click', '.vote-button', function(){
        voteForPost($(this));
        return false;
    });

    if($.fn.ajaxForm) {
        $('form.ajax-form').ajaxForm({beforeSend: setCSRFToken, success: addPostCallback, dataType: 'json'});
    }
    $('.send-post-button').click(function(){
        $('#post-form').submit();
        return false;
    });
    
    //
    $('.btn-post-form-open').click(function(){
        $('.posting__before').hide();
        $('.posting__form').show();
        return false;
    });
    
    $('.more-works').on('click', function(){
        var that = $(this);
        var offset = $('.work-item').length;
        var limit = that.attr('data-limit');
        var data = {'limit': limit, 'offset': offset}
            
        $.ajax({
            url: that.attr('data-url'),
            data: data
        }).done(function(data) {
            $('.work-list').append(data.html);
            if(data.last)
                that.hide();
        });        
    });
    
    $('.work-load').on('click', function(){
        var that = $(this);
        $.ajax({
            url: that.attr('data-url')
        }).done(function(data) {
            $('.work-container').html(data);
            //TODO: Show Work Container
        });                
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
        $('.vote-count-' + id).text(parseInt($('#vote-count-' + id).text())+1);
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
        $('.posting__form').hide();
        $('.posting__fail').show();
    }
}