$(document).ready(() => {
	let subForm = (e) => {
		e.preventDefault();
		let url = $(this).closest('form').attr('action');
		let data = $(this).closest('form').serialize();
		$.ajax({
			url: url,
			type: 'post',
			data: data,
			success: () => {
				window.location.reload();
			},
			error: (error) => {
				let errorsEl = $('#animationForm').find('.errors');
				errorsEl.append('<p>Error: ' + error.statusText + '</p>');
				errorsEl.show();
			}
		});
	}

	$('#animationForm').submit(subForm);
});