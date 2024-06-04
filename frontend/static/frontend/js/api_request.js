
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


		if (!urlInput.startsWith('http://') && !urlInput.startsWith('https://')) {
			urlInput = 'http://www.' + urlInput;
			urlInputElement.value = urlInput;
		}
		return urlInput;
	}

	function checkDomain(url) {
		let givenURL ;
		try {
			givenURL = new URL (url);
		} catch (error) {
		   return false; 
		}
		return true;
	  }

	function checkWhitespace(str) {
		let pattern = /\s/
		if (pattern.test(str)){
			return false;
		}
		return true;
	}

	function remove_old_feedback(urlInputElement){
		let url_feedback = document.getElementById('url_feedback');
		results_card.style.display = "none";
		if (url_feedback){
			url_feedback.style.display = "none";
		}
		urlInputElement.classList.remove('is-valid');
		urlInputElement.classList.remove('is-invalid');

	}

	const form = document.getElementById('url-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Evitar que el formulario se envíe de forma tradicional
		let validFeedback = document.getElementsByClassName("valid-feedback")[0];
		let urlInput = document.getElementById('url-input').value;
		let url_feedback = document.getElementById('url_feedback');
		const urlInputElement = document.getElementById('url-input');
        let isValid = true;
		remove_old_feedback(urlInputElement);
		urlInput = fix_url(urlInput, urlInputElement);
		if (!checkDomain(urlInput) || !checkWhitespace(urlInput)){
			isValid = false;
		}
	
        if (!isValid) {
			validFeedback.style.display  = 'none';
            form.classList.add('was-validated');
			urlInputElement.classList.add('is-invalid');
			url_feedback.innerText = '¡URL Inválida!';
			url_feedback.style.display = "block";
            return;
        } 
		
		else {
			validFeedback.style.display  = 'block';
			form.classList.add('was-validated');
			urlInputElement.classList.add('is-valid');
        }
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
			const data = await response.json();
			console.log(data);
            if (response.ok) {
				display_data(data);
				}
			else {
                console.error('Error en la petición:', response.statusText);
            }
        } catch (error) {
            console.error('Error en la petición:', error);
        }
    });
});
