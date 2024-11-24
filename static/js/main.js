let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

//Ensure Search Form Exists
if (searchForm) {
    for(let i =0;pageLinks.length > i; i++){
        pageLinks[i].addEventListener('click', function(e) {
            e.preventDefault()
            console.log('Pagination Click')

            //Get the Data Attribute
            let page = this.dataset.page
            console.log("PAGE : ", page)

            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

            searchForm.submit()
        })
    }

}

if (window.location.href.startsWith('http://127.0.0.1:8000/projects/update-project/') || 
        window.location.href.startsWith('http://127.0.0.1:8000/projects/create-project/')) {
    const textarea = document.getElementById('restricted-textarea');

        // Listen for input events
        textarea.addEventListener('input', (e) => {
            // Replace any character that is not a letter, number, or space
            textarea.value = textarea.value.replace(/[^a-zA-Z0-9 ]/g, '');
        })
    };