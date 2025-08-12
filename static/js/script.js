const form = document.querySelector('#formMain');
const submitBtn= document.querySelector("button");
const cancelBtn= document.querySelector("#cancelBtn");
const allinput= document.querySelector(".firstinput");
const formData = new FormData(document.getElementById('formMain'));
  
  const first_Name = document.querySelector('input[name="firstname"]');
  const last_Name = document.querySelector('input[name="lastname"]');
  const date_of_Birth = document.querySelector('input[name="dateofbirth"]');
  const gender = document.querySelectorAll('input[name="gender"]');
  const aadhar_number = document.querySelector('input[name="aadharnumber"]');
  const marital_status = document.querySelectorAll('input[name="Maritalstatus"]');
  const primary_phone_number = document.querySelector('input[name="primaryphonenumber"]');
  const current_address = document.querySelector('textarea[name="currentaddress"]');
  const permanent_address = document.querySelector('textarea[name="permanentaddress"]');
  const secondary_phone_number = document.getElementById('secondaryPhonenumber');
  const email = document.querySelector('input[name="email"]');
  const emergency_contact_name = document.querySelector('input[name="emergencycontactname"]');
  const emergency_contact_number = document.querySelector('textarea[name="emergencycontactnumber"]');
  const employment_id = document.querySelector('input[name="employmentid"]');
  const job_title = document.querySelector('select[name="jobtitle"]');
  const department = document.querySelector('select[name="department"]');
  const employment_start_date = document.querySelector('input[name="employmentstartdate"]');
  const employment_status = document.querySelector('select[name="employmentstatus"]');
  const reporting_manager = document.querySelector('input[name="reportingmanager"]');
  const bank_account = document.querySelector('textarea[name="bankaccount"]');
  const insurance_policy_number = document.querySelector('textarea[name="insurancepolicynumber"]');
  const tax_identification_number = document.querySelector('input[name="taxidentificationnumber"]');
  const blood_group = document.querySelector('select[name="bloodgroup"]');
  const known_allergies = document.querySelector('textarea[name="knownallergies"]');
  const special_instructions = document.querySelector('input[name="specialinstructions"]');
  const passport_number = document.querySelector('input[name="Passportnumber"]');
  const visa_details = document.querySelector('textarea[name="visadetails"]');
  const consent = document.querySelectorAll('input[name="consent"]');
  const date = document.querySelector('input[name="finaldate"]');
  const signature = document.querySelector('input[name="signature"]');
  const button = document.getElementById('mybutton');
  const messagElement = document.getElementById('message');
  document.getElementById('primary_phone_number').addEventListener('input', function() {
    var phonePattern = /^\d{10}$/;
    var primary_phone_number = this.value; 

    if (primary_phone_number && !phonePattern.test(primary_phone_number)) {
        alert('Invalid phone number in Primary Phone Number. Please enter a valid 10-digit number.');
    }
});

document.getElementById('secondary_phone_number').addEventListener('input', function() {
    var phonePattern = /^\d{10}$/;
    var secondary_phone_number = this.value; 

    if (secondary_phone_number && !phonePattern.test(secondary_phone_number)) {
        alert('Invalid phone number in Secondary Phone Number. Please enter a valid 10-digit number.');
    }
});

const phonePattern = /^\d{10}$/;
  
  if (!phonePattern.test(primary_phone_number.value)) {
    alertMessage.textContent = 'Invalid phone number in Primary Phone Number. Please enter a valid 10-digit number.';
    alertModal.show();
    return;
  }

  
  if (!phonePattern.test(secondary_phone_number.value)) {
    alertMessage.textContent = 'Invalid phone number in Secondary Phone Number. Please enter a valid 10-digit number.';
    alertModal.show();
    return;
  }
  function validateForm() {
    const aadharNumber = document.getElementById('aadharnumber').value;
    const aadharError = document.getElementById('aadhar-error');


    aadharError.style.display = 'none';

    if (!validateAadharNumber(aadharNumber)) {
        aadharError.style.display = 'block'; 
        alert('Invalid Aadhar number in Aadhar Number. Please enter a valid 12-digit number.');
        return false; 
    }

    return true; 
}
  
  function confSubmit(form) {
    if (confirm("Are you sure you want to submit the form?")) {
        form.submit();
    }
}
  function confCancel() {
    if (confirm("Are you sure you want to cancel the form?")) {
        alert("You have canceled the form submission.");
        document.getElementById("formMain").reset();
    } 
    else {
        alert("You chose to continue with the form submission.");
    }
} 

  const messageElement = document.getElementById('message');
  const alertModal = new bootstrap.Modal(document.getElementById('alertModal'));
  const alertMessage = document.getElementById('alertMessage');
    
    form.addEventListener('submit', function(event) {
      messageElement.textContent = ''; 
      let allValid = true;
      
      form.submit();
    })
  
  function validateAndSubmit(){
    function buttonclicked(){
      console.log('button clicked!');
      button.addEventListener('click',buttonclicked);
    }
    }
  document.getElementById('okBtn').addEventListener('click', function() {
      alertModal.hide();
  });

  document.getElementById('cancelBtn').addEventListener('click', function() {
      alertModal.hide();
      form.reset();
      alert('Form has been reset. Please re-enter your phone numbers.');
  });
    
    
    const requiredFields = [
        'firstname', 'lastname', 'dateofbirth', 'gender', 'aadharnumber',
        'Maritalstatus', 'primaryphonenumber', 'currentaddress','permanentaddress','secondaryPhonenumber','email',
        'emergencycontactname', 'emergencycontactnumber', 'employmentid',
        'jobtitle', 'department', 'employmentstartdate', 'employmentstatus',
        'bankaccount','insurancepolicynumber', 'taxidentificationnumber',
        'bloodgroup','Passportnumber','visadetails','finaldate'
    ];

        let allValid = true;

        requiredFields.forEach(field => {
            const input = form.querySelector(`[name="${field}"]`);
            if (!input || !input.value.trim()) {
                allValid = false;
                messageElement.textContent += `Please fill this ${field.replace(/([A-Z])/g, ' $1').toLowerCase()} field.\n`;
                alert ('Please fill this field');

            }
        });

        // if (!allValid) {
        //     event.preventDefault(); // Prevent form submission
        // }
document.getElementById("formMain").addEventListener("submit", function(event) {
   event.preventDefault();
  window.location.href = "success.html?message=Form submitted successfully!";
});
 console.log(index)
  submitBtn.addEventListener('click', (event) => {
    event.preventDefault();
        form.submit();
        

});
 
  cancelBtn.addEventListener('click', () => {
    form.reset();
    alert('Form has been reset');
});
