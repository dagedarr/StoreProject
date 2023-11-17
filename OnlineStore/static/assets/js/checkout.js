// Скрипт для окна сверху с ошибками
let messagesContainer = document.querySelector('.messages-container');
let messagesList = document.querySelector('.messages');

if (messagesList) {
  if (messagesList.children.length > 0) {
    messagesContainer.classList.add('show');
    setTimeout(function() {
      messagesContainer.classList.add('hide');
      messagesContainer.classList.remove('show');
    }, 2000);
  }
}

// Скрипт для всплывающего окна с оплатой
const paymentMethodSelect = document.getElementById('id_payment_method');
const onlinePaymentInfo = document.getElementById('online-payment-info');
const overlay = document.getElementById('overlay');
const closeBtn = document.getElementById('close-btn');

paymentMethodSelect.addEventListener('change', (event) => {
  if (event.target.value === 'card_online') {
    onlinePaymentInfo.style.display = 'block';
    overlay.style.display = 'block';
  } else {
    onlinePaymentInfo.style.display = 'none';
    overlay.style.display = 'none';
  }
});

closeBtn.addEventListener('click', () => {
  onlinePaymentInfo.style.display = 'none';
  overlay.style.display = 'none';
});