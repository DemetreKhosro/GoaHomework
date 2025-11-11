// 1) Event propagation ახსენით თქვენი სიტყვებით, დაწერეთ რას ნიშნავს კომენტარებით, მოიყვანეთ bubbling-ის და capturing-ის მაგალითი

// event propagation - როგორ მოედინება მოვლენები ელემენტებს შორის

const boxDiv = document.getElementById('boxDiv');
const btn = document.getElementById('btn');

// capturing გარედან შიგნით - შვილიდან მშობლამდე
boxDiv.addEventListener('click', capturingHandler, true);

// bubbling შიგნიდან გარეთ - მშობელიდან შვილამდე
boxDiv.addEventListener('click', bubblingHandler);
