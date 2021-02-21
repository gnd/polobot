<html>
<head>
<title>
    Polobot Graphs
</title>

<!-- META -->
<meta charset="UTF-8">
<meta id="description" content="polobot" />
<meta id="keywords" content="polobot" />
<meta id="revisit-after" content="1 days" />
<meta id="viewport" content="width=device-width,initial-scale=1" />

<!-- OPEN GRAPH -->
<meta property="og:locale" content="en_EN" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Polobot Graphs" />
<meta property="og:description" content="Polobot Graphs" />
<!-- <meta property="og:url" content="" /> 
<meta property="og:image" content="" />
<meta property="og:image:secure_url" content="" /> -->

<!-- MOMENT.JS -->
<script src="static/moment.js"></script>

<!-- CHART.JS -->
<script src="static/chart.min.js"></script>

<!-- PALETTE.JS -->
<script src="static/palette.js"></script>

<!-- MOBILE & DESKTOP STYLES -->
<link rel="stylesheet" media='screen and (min-width: 300px) and (max-width: 340px)' href="static/mobile.css?v=<?php echo filemtime('static/mobile.css'); ?>"/>
<link rel="stylesheet" media='screen and (min-width: 341px) and (max-width: 365px)' href="static/mobile.css?v=<?php echo filemtime('static/mobile.css'); ?>"/>
<link rel="stylesheet" media='screen and (min-width: 370px) and (max-width: 380px)' href="static/mobile.css?v=<?php echo filemtime('static/mobile.css'); ?>"/>
<link rel="stylesheet" media='screen and (min-width: 400px) and (max-width: 1000px)' href="static/mobile.css?v=<?php echo filemtime('static/mobile.css'); ?>"/>
<link rel="stylesheet" media='screen and (min-width: 1001px) and (max-width: 1300px)' href="static/desktop.css?v=<?php echo filemtime('static/desktop.css'); ?>"/>
<link rel="stylesheet" media='screen and (min-width: 1301px) and (max-width: 1599px)' href="static/desktop.css?v=<?php echo filemtime('static/desktop.css'); ?>"/>
<link rel="stylesheet" media='screen and (min-width: 1600px)' href="static/desktop.css?v=<?php echo filemtime('static/desktop.css'); ?>"/>

<!-- DATA -->
<script src="graph_data/last_position.js?v=<?php echo filemtime('graph_data/last_position.js'); ?>"></script>

<?php
    // compute last change to the code
    $max_code = filemtime('index.php');
    $max_code = max($max_code, filemtime('graphs/last_position.js'));
    // compute last change to the data
    $max_data = filemtime('graph_data/last_position.js');
?>

<!-- PREPARE GRAPHS -->
<script>
    var aspect_ratio = 2;                       // Desktop graph aspect ratio
    var aspect_ratio_mobile = 1.15;             // Mobile graph aspect ratio
    var fontsize = 12;
    var fontsize_mobile = 24;
    var pal_8 = palette('mpn65', 8);            // Generate palette
    moment.suppressDeprecationWarnings = true;
    
    function detect_client() {
        const mq = window.matchMedia('screen and (min-width: 300px) and (max-width: 340px)');
        if (mq.matches) {
            aspect_ratio = aspect_ratio_mobile;
        }
        const mq2 = window.matchMedia('screen and (min-width: 341px) and (max-width: 365px)');
        if (mq2.matches) {
            aspect_ratio = aspect_ratio_mobile;
        }
        const mq3 = window.matchMedia('screen and (min-width: 370px) and (max-width: 380px)');
        if (mq3.matches) {
            aspect_ratio = aspect_ratio_mobile;
        }
        const mq4 = window.matchMedia('screen and (min-width: 400px) and (max-width: 1000px)');
        if (mq4.matches) {
            aspect_ratio = aspect_ratio_mobile;
        }
    };
</script>

</head>
<body>
    <div class="top">
        <div class="header">
            <h1><span class="white">Polobot Graphs</span></h1>
            <h3><span class="medium_white">Simple graphing of tickers</span></h3>
            <span class="small_white">Ticker data taken from: <a href=https://docs.poloniex.com/#introduction>https://docs.poloniex.com/#introduction</a>.<br/>
            Last change: <?php echo date("d/m/y H:i", $max_code); ?> (code), <?php echo date("d/m/y H:i", $max_data); ?> (data)</span>
        </div>
    </div>
    <div class="graph_container">
        <a id="last_position_daily"></a>
        <div class="graph_filler">&nbsp;</div>
        <div class="canvas_container">
            <canvas id="last_position_daily_canvas" class="graph"></canvas>
            <a class="link" href="#last_position_daily">link</a>
        </div>
        <br class="clear"/>
    </div>
    <div class="graph_container">
        <a id="last_position_weekly"></a>
        <div class="graph_filler">&nbsp;</div>
        <div class="canvas_container">
            <canvas id="last_position_weekly_canvas" class="graph"></canvas>
            <a class="link" href="#last_position_weekly">link</a>
        </div>
        <br class="clear"/>
    </div>
    <div class="graph_container">
        <a id="last_position_monthly"></a>
        <div class="graph_filler">&nbsp;</div>
        <div class="canvas_container">
            <canvas id="last_position_monthly_canvas" class="graph"></canvas>
            <a class="link" href="#last_position_monthly">link</a>
        </div>
        <br class="clear"/>
    </div>
    <div class="bottom_container">
        <div class="bottom_nav">
            Polobot Graphs
		</div>
    </div>
</body>

<script>
    // detect if mobile or desktop
    detect_client();
</script>
<!-- last position -->
<script src="graphs/last_position.js?v=<?php echo filemtime('graphs/last_position.js'); ?>"></script>
</html>
