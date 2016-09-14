/**
 * Created by ywh on 2016/9/15.
 */
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('app', { title: '辉大微博' });
});

module.exports = router;
