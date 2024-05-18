window.addEventListener('DOMContentLoaded', () => {

   // Query the elements that have data-content as attribute
   const els = document.querySelectorAll('[data-content]');

   // Stop the function if there is no elements found
   if (els.length < 1) return;

   // Set the media query
   const mediaQuery = window.matchMedia('(max-width: 768px)')

   // Function
   const replaceContent = (e) => {

      let content;

      // Loop inside each element
      els.forEach(el => {

         // Parse the content attribute
         const attr = JSON.parse(el.dataset.content);

         // Desktop text
         content = attr.desktop;

         // Check if the media query is true
         if (e.matches) {

            // if the media query is true, change the mobile text
            content = attr.mobile;

         }

         // Change the text
         el.textContent = content;
      })

   }

   // Resize
   mediaQuery.addEventListener('change', replaceContent);

   // On load
   replaceContent(mediaQuery);

})// JavaScript Document