//Ember
try {
    console.log("Ember version: " + Ember.VERSION);
} catch (e) {
    if (e instanceof ReferenceError) {
        console.log("Ember doesn't exist on this website")
    }
}

//AngularJS
try {
    const elements = getAllAngularRootElements();
    const angularVersion = elements[0].attributes['ng-version'];
    console.log("Angular version: " + angularVersion);
} catch (e) {
    if (e instanceof ReferenceError) {
        console.log("Angular doesn't exist on this website")
    }
}

//React
try {
    console.log("React version: " + React.version);
} catch (e) {
    if (e instanceof ReferenceError) {
        console.log("React doesn't exist on this website")
    }
}

//VueJS
try {
    Vue.config.devtools = true;
    console.log("Vue version: " + Vue.version);
} catch (e) {
    if (e instanceof ReferenceError) {
        console.log("VueJS doesn't exist on this website")
    }
}

//Ext JS
try {
    console.log("Ext version: " + Ext.getVersion());
} catch (e) {
    if (e instanceof ReferenceError) {
        console.log("Ext JS doesn't exist on this website")
    }
}

//Knockout.js
try {
    console.log("Knockout version: " + ko.version);
} catch (e) {
    if (e instanceof ReferenceError) {
        console.log("Knockout.js doesn't exist on this website")
    }
}

//Meteor
try {
    console.log("Meteor version: " + Meteor.release);
} catch (e) {
    if (e instanceof ReferenceError) {
        console.log("Meteor doesn't exist on this website")
    }
}

//Svelte
try {
    console.log("Svelte version: " + svelte.VERSION);
} catch (e) {
    if (e instanceof ReferenceError) {
        console.log("Svelte doesn't exist on this website")
    }
}

//jQuery
try {
    console.log("jQuery Version: " + $.fn.jquery)
} catch (e) {
    if (e instanceof TypeError) {
        console.log("jQuery doesn't exist on this website")
    }
}

//Get all js scripts in <script> tags
const getScripts = function() {
    const scripts = document.querySelectorAll('script');
    scripts.forEach((script) => {
        if (script.src) {
            console.log(`Script: ${script.src}`);
        }
    });
};

getScripts();

//Get all css libraries
const getStyles = function() {
    const styles = document.querySelectorAll('link');
    styles.forEach((link) => {
        if (link.rel === 'stylesheet') {
            console.log(`CSS: ${link.getAttribute('href')}`)
        }
    });
};

getStyles();
