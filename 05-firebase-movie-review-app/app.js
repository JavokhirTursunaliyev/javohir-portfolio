const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "SENDER_ID",
    appId: "APP_ID"
  };
  
  firebase.initializeApp(firebaseConfig);
  const db = firebase.firestore();
  const reviewsRef = db.collection("reviews");
  
  document.getElementById("review-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const movie = document.getElementById("movie").value;
    const rating = parseInt(document.getElementById("rating").value);
    const director = document.getElementById("director").value;
    const releaseDate = document.getElementById("releaseDate").value;
  
    await reviewsRef.add({ movie, rating, director, releaseDate });
    e.target.reset();
    fetchReviews();
  });
  
  async function fetchReviews() {
    const sortField = document.getElementById("sortField").value;
    const snapshot = await reviewsRef.orderBy(sortField).get();
    const table = document.getElementById("reviewsTable");
    table.innerHTML = "";
  
    snapshot.forEach((doc) => {
      const data = doc.data();
      const row = document.createElement("tr");
  
      row.innerHTML = `
        <td>${data.movie}</td>
        <td>${data.rating}</td>
        <td>${data.director}</td>
        <td>${data.releaseDate}</td>
        <td>
          <button onclick="editReview('${doc.id}', '${data.movie}', ${data.rating}, '${data.director}', '${data.releaseDate}')">Edit</button>
          <button onclick="deleteReview('${doc.id}')">Delete</button>
        </td>
      `;
  
      table.appendChild(row);
    });
  }
  
  async function deleteReview(id) {
    await reviewsRef.doc(id).delete();
    fetchReviews();
  }
  
  function editReview(id, movie, rating, director, releaseDate) {
    document.getElementById("movie").value = movie;
    document.getElementById("rating").value = rating;
    document.getElementById("director").value = director;
    document.getElementById("releaseDate").value = releaseDate;
  
    document.getElementById("review-form").onsubmit = async (e) => {
      e.preventDefault();
      await reviewsRef.doc(id).set({
        movie: document.getElementById("movie").value,
        rating: parseInt(document.getElementById("rating").value),
        director: document.getElementById("director").value,
        releaseDate: document.getElementById("releaseDate").value
      });
      e.target.reset();
      document.getElementById("review-form").onsubmit = addReview;
      fetchReviews();
    };
  }
  
  const addReview = document.getElementById("review-form").onsubmit;
  fetchReviews();
  