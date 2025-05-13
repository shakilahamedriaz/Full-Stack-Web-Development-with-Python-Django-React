// products = [
//     {
//         "id": 1,
//         "name": "Product 1",
//         "price": 10.00,
//         "description": "Description for Product 1",
//         "image": "https://picsum.photos/300/200?random=1",
//     },
//     {
//         "id": 2,
//         "name": "Product 2",
//         "price": 20.00,
//         "description": "Description for Product 2",
//         "image": "https://picsum.photos/300/200?random=2",
//     },
//     {
//         "id": 3,
//         "name": "Product 3",
//         "price": 30.00,
//         "description": "Description for Product 3",
//         "image": "https://picsum.photos/300/200?random=3",
//     },
//     {
//         "id": 4,
//         "name": "Product 4",
//         "price": 40.00,
//         "description": "Description for Product 4",
//         "image": "https://picsum.photos/300/200?random=4",
//     }
// ]

// const productList = document.getElementById('product-list');

// products.forEach(product => {
//     const productCard = `
//         <div class="bg-white rounded-lg shadow-md overflow-hidden">
//             <img src="${product.image}" alt="${product.name}" class="w-full h-48 object-cover">
//             <div class="p-4">
//                 <h2 class="font-bold text-xl mb-2">${product.name}</h2>
//                 <p class="text-gray-700 mb-2">${product.description}</p>
//                 <p class="font-bold text-lg text-blue-600">$${product.price}</p>
//                 <button class="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
//                     Add to Cart
//                 </button>
//             </div>
//         </div>
//     `
//     productList.innerHTML = productList.innerHTML + productCard;
// });



//  Fetch Function + REST API
const productList = document.getElementById('product-list');

fetch('https://fakestoreapi.com/products')
    .then((response) => response.json())
    .then((products) => {
        products.forEach((product) => {
            const productCard = `
                <div class="bg-white rounded-lg shadow-md overflow-hidden">
                    <img src="${product.image}" alt="${product.name}" class="w-full h-48 object-cover">
                    <div class="p-4">
                        <h2 class="font-bold text-xl mb-2">${product.title}</h2>
                        <p class="text-gray-700 mb-2">${product.description}</p>
                        <p class="font-bold text-lg text-blue-600">$${product.price}</p>
                        <button class="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                            Add to Cart
                        </button>
                    </div>
                </div>
            `;
            productList.innerHTML += productCard;
            // a = 10
            // a = a + 2
        });
    })
    .catch(error => console.error('Error fetching products:', error));

// GET
// POST

// PUT / PATCH
// DELETE
