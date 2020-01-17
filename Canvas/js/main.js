$(function(){

    function transform(strokes) {
      for (var i = 0; i < strokes.length; ++i)
        for (var j = 0, stroke = strokes[i]; j < stroke.length; ++j)
            strokes[i][j] = [ strokes[i][j][0], strokes[i][j][1] ];
      return strokes;
    };

    function strokesToScg(strokes) {
      var scg = 'SCG_INK\n' + strokes.length + '\n';
      strokes.forEach(function (stroke) {
        scg += stroke.length + '\n';
        stroke.forEach(function (p) {
          scg += p[0] + ' ' + p[1] + '\n';	
        })
      })
      return scg;
    };

    function convertStrokes() {
      var strokes = $canvas.sketchable('strokes');
      strokes = transform(strokes);
      var textToSave = strokesToScg(strokes);
      var hiddenElement = document.createElement('a');
      hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
      hiddenElement.target = '_blank';
      hiddenElement.download = 'Output.scgink';
      hiddenElement.click();
    };

    function urlParam(name) {
      var results = new RegExp('[\\?&]' + name + '=([^&#]*)').exec(top.window.location.href); 
      return (results !== null) ? results[1] : undefined;
    };
    
    var $canvas = $('#drawing-canvas').sketchable({
      graphics: {
        strokeStyle: "red",
        firstPointSize: 2
      }
    });
    
    function clearStrokes() {
      $canvas.sketchable('clear');
      $('.result').empty();
    };

    $('a#clear').on("click", function(e){
      e.preventDefault();
      clearStrokes();
    });

    $('a#convert').on("click", function(e){
      e.preventDefault();
      convertStrokes();
    }); 

    $('a#undo').on("click", function(e){
      e.preventDefault();
      $canvas.sketchable('undo');
    });

    $('a#redo').on("click", function(e){
      e.preventDefault();
      $canvas.sketchable('redo');
    });
    
});
