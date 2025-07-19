function valid() {
  let fname = document.getElementById("id_firstname").value.trim();
  let lname = document.getElementById("id_lastname").value.trim();
  let email = document.getElementById("id_email").value.trim();
  let phone = document.getElementById("id_phone").value.trim();

  let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


  if (fname === "") {
    alert("Please enter Firstname");
    return false;
  }
  if (!isNaN(fname)) {
    alert("Firstname should not be numeric");
    return false;
  }

 
  if (lname === "") {
    alert("Please enter Lastname");
    return false;
  }
  if (!isNaN(lname)) {
    alert("Lastname should not be numeric");
    return false;
  }


  if (email === "") {
    alert("Please enter Email");
    return false;
  }
  if (!emailPattern.test(email)) {
    alert("Please enter a valid email");
    return false;
  }


  if (phone === "") {
    alert("Please enter phone");
    return false;
  }
  if (isNaN(phone)) {
    alert("Phone must contain only numbers");
    return false;
  }
  if (phone.length !== 10) {
    alert("Phone number should be exactly 10 digits");
    return false;
  }

  return true;
}
