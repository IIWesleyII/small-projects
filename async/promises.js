const posts = [
    {title : 'Post One', body : 'post 1'},
    {title : 'Post Two', body : 'post 2'}
];

function getPosts(){
    setTimeout(() => {
        let output = '';
        posts.forEach((post, index) => {
            output += `<li>${post.title}</li>`;
        });
        document.body.innerHTML = output;
    }, 1000);
}
function createPost(post, callback){
    //when something goes right call resolve
    // when something goes wrong call reject
    return new Promise( (resolve, reject) =>{
        setTimeout(() => {
            posts.push(post);

            const error = false;

            if(!error){
                resolve();
            }else{
                reject('Error: something went wrong.');
            }
        }, 2000);

    })
}
createPost({title : 'Post Three', body : 'Post 3!'})
    .then(getPosts)
    .catch(err => console.log(err));

