document.addEventListener('DOMContentLoaded', () => {

	function display_data(data){
		let shortened_url = document.getElementById("shortened_url");
		let shortened_url_p = document.getElementById("shortened_url_p");
		let number_clicks = document.getElementById("number_clicks");
		let number_clicks_p = document.getElementById("number_clicks_p");
		let last_click = document.getElementById("last_click");
		let last_click_p = document.getElementById("last_click_p");
		let results_card = document.getElementById("results_card");
		let expiration_date_p = document.getElementById("expiration_date_p");
		let expiration_date = document.getElementById("expiration_date");

		results_card.style.display = "block";
		try{
			shortened_url_p.innerHTML = "Link corto: ";
			shortened_url.innerHTML =  data.short_link;
			shortened_url.href =  data.short_link

			number_clicks_p.innerHTML = "Clicks: ";
			number_clicks.innerHTML = data.clicks;

			expiration_date_p.innerHTML = "Expira el: ";
			expiration_date.innerHTML = data.expiration;

			last_click_p.innerHTML = "Último click: ";
			if (data.last_click == null) {
				last_click.innerHTML = 'Nunca';
			}
			else {
				last_click.innerHTML = data.last_click;
			}
		
			}
		catch (error) {
					console.error('Error en la petición:', error);
				}
	}

	function fix_url(urlInput, urlInputElement){
		// Añadir 'http://' si no está presente

		if (urlInput.startsWith('www.')) {
			urlInput = 'http://' + urlInput;
			urlInputElement.value = urlInput;
		}

		else if (!urlInput.startsWith('http://www.') && !urlInput.startsWith('https://www.')) {
			urlInput = 'http://www.' + urlInput;
			urlInputElement.value = urlInput;
		}
		return urlInput;
	}

	function checkDomain(str){
		let pattern = /\.[a-zA-Z]+/;
		if (! pattern.test(str)){
			url_feedback.innerHTML = "¡URL Inválida!";
			return false;
		}
		return true;
	}

	function checkWhitespace(str) {
		let pattern = /\s/
		if (pattern.test(str)){
			console.log("Yeah 2 here");
			url_feedback.innerText = '¡URL Inválida!';
			return false;
		}
		return true;
	}

	function remove_old_feedback(urlInputElement){
		url_feedback.innerHTML = "";
		shortened_url_p.innerHTML = "";
		shortened_url.innerHTML = "";
		shortened_url.href = "";
		urlInputElement.classList.remove('is-valid');
		urlInputElement.classList.remove('is-invalid');

	}

	const form = document.getElementById('url-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Evitar que el formulario se envíe de forma tradicional
		let urlInput = document.getElementById('url-input').value;
		let url_feedback = document.getElementById('url_feedback');
		const urlInputElement = document.getElementById('url-input');
		

        let isValid = true;
		remove_old_feedback(urlInputElement);
        if (!checkDomain(urlInput) || !checkWhitespace(urlInput)){
            isValid = false;
        }

        if (!isValid) {
			
            urlInputElement.classList.add('is-invalid');
            form.classList.add('was-validated');
            return;
        } else {
			
            urlInputElement.classList.add('is-valid');
			form.classList.add('was-validated');
			urlInput = fix_url(urlInput, urlInputElement);
        }

		console.log(urlInput);
        const payload = {
            link: urlInput
        };
        try {
            const response = await fetch('/api/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (response.ok) {
                const data = await response.json();
                console.log('URL shortened:', data);
				display_data(data);
				}
			else {
				console.log(response.json())
                console.error('Error en la petición:', response.statusText);
            }
        } catch (error) {
            console.error('Error en la petición:', error);
        }
    });
});
