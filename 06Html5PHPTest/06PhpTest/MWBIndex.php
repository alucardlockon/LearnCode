<!DOCTYPE html>
<meta charset="utf-8">
<html>
<head>
  <?php 
  require_once 'utils\mysqlUtils.php';
  $mysqlutil=new mysql(); 
  #$mysqlutil->connect();
   ?>
  <title>辉大微博(MyWeiBo)</title>
  <style type="text/css">
    /*body {font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 12px;color: #1d1007; line-height:24px} */
    .navbar{
      font-size: 20px;
    }
    .navbar li{
      float: left;
      width: 25%;
    }
  </style>
  <link href="css/bootstrap.min.css" rel="stylesheet" />
  <link href="css/bootstrap-theme.min.css" rel="stylesheet" />
</head>
<body>
  <script src="js/bootstrap.min.js"></script>
  <header>
  <h1>辉大微博</h1>
  </header>
  <nav>
    <ul class="navbar">
      <li><a href="MWBIndex.html">首页</a></li>
      <li><a href="MWBUser.html">我的微博</a></li>
      <li><a href="MWBFollow.html">我的关注</a></li>
      <li><a href="MWBLogout.action">退出登录</a></li>
    </ul>
  </nav>
  <aside style="float:right">
    <h2>热门动态</h2>
    <section>
      <h3>微博04</h3>
      <p>这是一条微博。</p>
    </section>
    <section>
      <h3>微博05</h3>
      <p>这是一条微博。</p>
    </section>
  </aside>
  <articles>
    <h3>微博01</h3>
    <p>这是一条微博。</p>
  </articles>
  <articles>
    <h3>微博02</h3>
    <p>这是一条微博。</p>
  </articles>
  <articles>
    <h3>微博03</h3>
    <p>这是一条微博。</p>
  </articles>
  <footer>
    Developed by PHP。
    <address>Alucardlockon</address>
  </footer>
</body>

</html>