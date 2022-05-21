function loadTable() {
    const xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://127.0.0.1:5000/v1/data");
    xhttp.send();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var trHTML = ''; 
        const objects = JSON.parse(this.responseText);
        for (let object of objects) {
          trHTML += '<tr>'; 
          trHTML += '<td>'+object['id']+'</td>';
          trHTML += '<td>'+object['fname']+'</td>';
          trHTML += '<td>'+JSON.parse(object['lname']).cpf+'</td>';
          trHTML += '<td>'+object['username']+'</td>';
          trHTML += '<td>'+JSON.parse(object['group'])+'</td>';
          trHTML += '<td>'+object['group_name']+'</td>';
          trHTML += '<td>'+JSON.parse(object['telephone']).telephone+'</td>';
          trHTML += '<td>'+JSON.parse(object['birthday']).birthday+'</td>';
          trHTML += '<td>'+JSON.parse(object['address']).street+' '+
                           JSON.parse(object['address']).number+', '+
                           JSON.parse(object['address']).city+', '+
                           JSON.parse(object['address']).state+' '+
                           JSON.parse(object['address']).zip_code+'</td>';
          trHTML += '<td><button type="button" class="btn btn-outline-secondary" onclick="showUserEditBox('+object['id']+')">Edit</button>';
          trHTML += '<button type="button" class="btn btn-outline-danger" onclick="userDelete('+object['id']+')">Del</button></td>';
          trHTML += "</tr>";
        }
        document.getElementById("mytable").innerHTML = trHTML;
      }
    };
  }
  
  loadTable();
  
  function showUserCreateBox() {
    Swal.fire({
      title: 'Adicionar Galerners',
      html:
        '<input id="id" type="hidden">' +
        '<input id="fname" class="swal2-input" placeholder="Name">' +
        '<input id="lname" class="swal2-input" placeholder="CPF">' +
        '<input id="email" class="swal2-input" placeholder="Email">' +
        '<input id="group" class="swal2-input" placeholder="Grupo">' +
        '<input id="group_name" class="swal2-input" placeholder="Grupo nome">' +
        '<input id="telephone" class="swal2-input" placeholder="Telefone">'+
        '<input id="birthday" class="swal2-input" placeholder="Data Nascimento">'+
        '<input id="street" class="swal2-input" placeholder="Rua">'+
        '<input id="number" class="swal2-input" placeholder="Numero">'+
        '<input id="city" class="swal2-input" placeholder="Cidade">'+
        '<input id="state" class="swal2-input" placeholder="Estado">'+
        '<input id="zip_code" class="swal2-input" placeholder="Cep">',

      focusConfirm: false,
      preConfirm: () => {
        //Swal.fire('ERROR');
        userCreate();
      }
    })
  }
  
  function userCreate() {
    const username = document.getElementById("id").value;
    const fname = document.getElementById("fname").value;
    const lname = document.getElementById("lname").value;
    const email = document.getElementById("email").value;
    const group = document.getElementById("group").value;
    const group_name = document.getElementById("group_name").value;
    const telephone = document.getElementById("telephone").value;
    const birthday = document.getElementById("birthday").value;
    const street = document.getElementById("street").value;
    const number = document.getElementById("number").value;
    const city = document.getElementById("city").value;
    const state = document.getElementById("state").value;
    const zip_code = document.getElementById("zip_code").value;



  

    const xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:5000/v1/data");
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ 
      "id": id, "fname": fname, "lname": lname, "email": email, "group": group, 
      "group_name": group_name, "telephone": telephone, "birthday": birthday, 
      "street": street, "number": number, "city": city, "state": state,
      "zip_code": zip_code
    }));
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const objects = JSON.parse(this.responseText);
        Swal.fire(objects['message']);
        loadTable();
      }
    };
  }
  
  function userDelete(id) {
    const xhttp = new XMLHttpRequest();
    xhttp.open("DELETE", "http://127.0.0.1:5000/v1/data/"+id);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
     xhttp.send(JSON.stringify({ 
       "id": id
     }));
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4) {
        const objects = JSON.parse(this.responseText);
        Swal.fire(objects['message']);
        loadTable();
      } 
    };
  }
  
  function showUserEditBox(id) {
    const xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://127.0.0.1:5000/v1/data/"+id);
    xhttp.send();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const objects = JSON.parse(this.responseText);
        const user = objects;
        Swal.fire({
          title: 'Edit User',
          html:
            '<input id="id" type="hidden" value="'+ id+'">' +
            '<input id="fname" class="swal2-input" placeholder="Name" value="'+user['name']+'">' +
            '<input id="lname" class="swal2-input" placeholder="CPF" value="'+JSON.parse(user['cpf']).cpf+'">' +
            '<input id="email" class="swal2-input" placeholder="Email" value="'+user['email']+'">' +
            '<input id="group" class="swal2-input" placeholder="Grupo" value="'+user['group']+'">' +
            '<input id="group_name" class="swal2-input" placeholder="Grupo nome" value="'+user['group_name']+'">' +
            '<input id="telephone" class="swal2-input" placeholder="Telefone" value="'+JSON.parse(user['telephone']).telephone+'">'+
            '<input id="birthday" class="swal2-input" placeholder="Data Nascimento" value="'+JSON.parse(user['birthday']).birthday+'">'+
            '<input id="street" class="swal2-input" placeholder="Rua" value="'+JSON.parse(user['address']).street+'">'+
            '<input id="number" class="swal2-input" placeholder="Numero" value="'+JSON.parse(user['address']).number+'">'+
            '<input id="city" class="swal2-input" placeholder="Cidade" value="'+JSON.parse(user['address']).city+'">'+
            '<input id="state" class="swal2-input" placeholder="Estado" value="'+JSON.parse(user['address']).state+'">'+
            '<input id="zip_code" class="swal2-input" placeholder="Cep" value="'+JSON.parse(user['address']).zip_code+'">',
          focusConfirm: false,
          preConfirm: () => {
            userEdit();
          }
        })
      }
    };
  }
  
  function userEdit() {
    const id = document.getElementById("id").value;
    const fname = document.getElementById("fname").value;
    const lname = document.getElementById("lname").value;
    const email = document.getElementById("email").value;
    const group = document.getElementById("group").value;
    const group_name = document.getElementById("group_name").value;
    const telephone = document.getElementById("telephone").value;
    const birthday = document.getElementById("birthday").value;
    const street = document.getElementById("street").value;
    const number = document.getElementById("number").value;
    const city = document.getElementById("city").value;
    const state = document.getElementById("state").value;
    const zip_code = document.getElementById("zip_code").value;
    const xhttp = new XMLHttpRequest();
    xhttp.open("PUT", "http://127.0.0.1:5000/v1/data/"+id);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ 
      "fname": fname, "lname": lname, "email": email, "group": group, 
      "group_name": group_name, "telephone": telephone, "birthday": birthday, 
      "street": street, "number": number, "city": city, "state": state,
      "zip_code": zip_code
    }));
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const objects = JSON.parse(this.responseText);
        Swal.fire(objects['message']);
        loadTable();
      }
    };
  }
  