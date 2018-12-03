new Vue({
    el: '#app',
    data: {
      columns: ['Tanggal', 'Max', 'Min', 'Perbedaan', 'Detail', 'Update'],
      listBerat: [''],
      current: [],
      avemax: 0,
      avemin: 0,
      isCreate: 0,
      isEdit: 0,
      isShow: 0
    },
    mounted(){
        this.update();
    },
    methods: {
        update(){            
            this.listBerat = [];
            axios.get("http://127.0.0.1:5544/berat").then(response => {
                this.listBerat = response.data;
            }); 
            axios.get("http://127.0.0.1:5544/ratarata").then(response => {
                this.avemax = response.data.max;
                this.avemin = response.data.min;
            }); 
        },
        clickCreate(row){
            this.current = [];
            this.isCreate = 1;
        },
        createData(){
            payload = {'tanggal': this.current['tanggal'], 'max': this.current['max'], 'min': this.current['min']};
            axios.post("http://127.0.0.1:5544/berat", payload).then(response => {
                this.isCreate = 0;
                this.update();
            }); 
        },

        clickShow(row){
            this.current = row;
            this.isShow = 1;
        },

        clickEdit(row){
            this.current = row;
            this.isEdit = 1;
        },
        saveEdit(){
            payload = {'tanggal': this.current['tanggal'], 'max': this.current['max'], 'min': this.current['min']};
            axios.post("http://127.0.0.1:5544/berat", payload).then(response => {
                this.isEdit = 0;
                this.update();
            }); 
        },
        clickDelete(row){
            axios.post("http://127.0.0.1:5544/hapus", {'tanggal':this.current.tanggal}).then(response => {
                this.isEdit = 0;
                this.update();
            }); 
        }
    }
  });