$(function (){

    var $data = $('#text');

    $.ajax({
      type: 'GET',
      url: 'https://api.telegram.org/bot234316785:AAGxNpXrEQu46bSPlN51MMYBRdADuYwo3yA/getupdates',
      success: function(data){
        setInterval(function() {
          $.each(data['result'], function(i, chat) {
              $data('<li>Text: '+ chat['message']['text'] +'</li>').fadeIn("slow")
          });
        }, 1000);
        // $.for(key in data['result']{
        //   $data.append('<li>Text: '+ key['message']['text'] +'</li>')
        // });
        // $.each(data['result'], function(i, chat) {
        //     $data.append('<li>Text: '+ chat['message']['text'] +'</li>')
        // });
        // console.log('success', data['result'].length);
        // console.log('success', data['result'][data['result'].length-1]['message']['text']);
      }
    });

});
