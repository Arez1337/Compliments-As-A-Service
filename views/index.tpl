<html>
<head>
<style>
body {
  background: url({{backgroundImage}})no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
.vertical-alignment-helper {
    display:table;
    height: 100%;
    width: 100%;
    pointer-events:none; /* This makes sure that we can still click outside of the modal to close it */
}
.vertical-align-center {
    /* To center vertically */
    display: table-cell;
    vertical-align: middle;
    pointer-events:none;
}

.modal-dialog { /* Width */
    max-width: 100%;
    width: auto;
    display: inline-block;
    max-width: fit-content;
}

</style>

<!-- Gotta set the viewport for mobile devices! -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>


<script type="text/javascript">
    $(window).on('load', function() {
        $('#compliment').modal('show');
    });
</script>

<title>
{{title}}
</title>
</head>
<body class="text-center">
  <div class="vertical-alignment-helper">
    <div class="vertical-align-center">
    <div class="modal-dialog modal-dialog-centered modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-body">
            {{compliment}}
          </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>
