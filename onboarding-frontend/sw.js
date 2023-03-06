

self.addEventListener('push', function(event) {
  console.log('[Service Worker] Push Received.');
  console.log('[Service Worker] Push had this data: "${event.data.text()}"');
  const message = event.data.json();
  const title = message["title"];
  const options = {
    body: message["desc"]
  };
  event.waitUntil(self.registration.showNotification(title, options));
});

