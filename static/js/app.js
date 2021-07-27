let getCookie = function() { // for django csrf protection
    let cookieValue = null,
        name = "csrftoken";
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};


const cartActive = (slug, quantity = 1, action) => {
    let token = getCookie();
    axios({
        method: action,
        url: cartActiveUrl,
        headers: {
            'accept': 'application/json',
            'X-CSRFToken': token,
        },
        data: {
            slug: slug,
            quantity: quantity,
        }
    }).then(res => {
        let { message } = res.data
        Swal.fire(
            'Item added to cart!',
            message,
            'success'
        )
    }).catch(err => {
        Swal.fire(
            'Some error occured',
            err.response.data.detail,
            'error'
        )
    })
}