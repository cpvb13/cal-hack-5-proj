
function sendGet(route, cb) {
	var url = API_BASE_URL + route;
	$('#requests-content').append('GET ' + url);
	$('#requests-content').append('<br/>');
	$.get(url, function(data) {
		$('#responses-content').append(JSON.stringify(data) + ' (status 200)');
		$('#responses-content').append('<br/>');
		if (cb) cb(data);
	});
}

function sendPost(route, d, cb) {
	var url = API_BASE_URL + route;
	$('#requests-content').append('POST ' + url + ' ' + JSON.stringify(d));
	$('#requests-content').append('<br/>');
	$.post(url, d, function(data) {
		console.log(data)
		console.log(d)
		$('#responses-content').append('' + JSON.stringify(data) + ' (status 200)');
		$('#responses-content').append('<br/>');
		if (cb) cb(data);
	});
}

$(document).ajaxError(function(event, jqxhr, settings, error) {
	$('#responses-content').append('Error status ' + jqxhr.status + ' <br/>');
});

$(function() {
	sendGet('/counter', function(data) {
		$('#number').text(data);
	});

	

	$('#addd').click(function() {
		var text1 = $('#iteminput').val();
		console.log(text1)
		sendPost('/add', {}, function() {
			console.log('hey')
			sendPost('/item',{field1: text1}, function(text) {
				console.log(text)
				sendGet('/counter', function(number) {
					console.log('a')
					console.log(text, number)
					number = Number(number)
					if (number === 1) {
						$('#box').text(text1);
					} else if (number === 2) {
						$('#number1').text(text1);
					} else if (number === 3) {
						$('#number2').text(text1);
					} else if (number === 4) {
						$('#number3').text(text1);
					} else if (number === 5) {
						$('#number4').text(text1);
					}
					console.log('b')
				});	
			});
		});
	});

	$('#search').click(function() {
		sendPost('/search', {}, function() {
			sendGet('/counter', function(data) {
				$('#number').text(data);
			});
		});
	});
});
