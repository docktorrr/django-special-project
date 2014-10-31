$(function() {

    $('.quiz-next-button').click(function() {
        var $question = $('.quiz-question').filter(':visible');
        if ($question.find('input[type=radio]:checked').length) {
            if($question.is(':last-child')) {
                $('#quiz-form').submit();
            } else {
                $question.fadeOut(300, function(){$question.next('.quiz-question').fadeIn(300);});
                return false;
            }
        } else {
            alert("Вы не выбрали ответ");
            return false;
        }
    });

    $('.answer').click(function(){
        $this = $(this);
        $this.parents('.quiz-question').find('input[type="radio"]').prop('checked', false);
        $this.find('input[type="radio"]').prop('checked', true);
        $this.addClass('active');
        $this.siblings().addClass('unactive');
        $this.parents('.answers').children().unbind( "click" );        
        $.ajax({
            url: $this.parents('.answers').attr('data-url')
        }).done(function(data) {
            $.each($.parseJSON(data), function(index, value) {                
                var $current =  $this.parents('.answers').children().eq(index);
                if(typeof $current != 'undefined') {
                    if(value > 0)
                        $current.addClass('correct');
                    else
                        $current.addClass('incorrect');
                }
            });
        });
        return false;
    });
    
});