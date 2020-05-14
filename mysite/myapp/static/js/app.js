$(document).foundation()


var app4 = new Vue({
    el: '#app-4',
    data: {
      properties: [],
      seen:true,
      unseen:false
    },
    //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
    created: function() {
          this.fetchPropertyList();
          this.timer = setInterval(this.fetchPropertyList, 10000);
    },
    methods: {
      fetchPropertyList: function() {
          // $.get('/', function(property_list) {
          //     this.properties = property_list.properties;
          //     console.log(property_list);
          // }.bind(this));
          axios
            .get('/')
            // .then(response => console.log(response.data))
            .then(response => (this.properties = response.data.properties))
          console.log(this.properties)
          this.seen=false
          this.unseen=true
      },
      cancelAutoUpdate: function() { clearInterval(this.timer) }
    },
    beforeDestroy() {
      // clearInterval(this.timer)
      this.cancelAutoUpdate();
    }

  })
