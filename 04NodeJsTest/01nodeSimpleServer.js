var http=require('http');
var querystring=require('querystring');
exports.runServer=function(port){
  port=port||8080;
  var server=http.createServer(function(req,res){
    var _postData='';
    req.on('data',function(chunk){
      _postData+=chunk;
    })
    .on('end',function(){
      req.post=querystring.parse(_postData);
      handlerRequest(req,res);
    });
  }).listen(port);
  console.console.log(('Server running at http://127.0.0.1:'+port+'/'));
};
