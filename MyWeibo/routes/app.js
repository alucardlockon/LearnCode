/**
 * Created by ywh on 2016/9/15.
 */
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/myWeiBo', function(req, res, next) {
    res.render('myWeiBo', { title: '辉大微博' });
});

router.get('/myFollow', function(req, res, next) {
    res.render('myFollow', { title: '辉大微博' });
});

router.get('/logout', function(req, res, next) {

});


module.exports = router;
