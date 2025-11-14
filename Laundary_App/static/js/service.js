<script>
function openBookingForm(serviceName) {
  document.getElementById('bookingForm').style.display = 'flex';
  document.getElementById('serviceType').value = serviceName;
}

function closeBookingForm() {
  document.getElementById('bookingForm').style.display = 'none';
}
</script>
