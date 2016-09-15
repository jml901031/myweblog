new Vue({
    el: '#loginform',
    data: {
        email: '',
        password: '',
        message: ''
    },
    methods: {
        login: function() {
            this.email = this.email.trim();
            var self = this;
            $.ajax('/auth', {
                data: {
                    email: self.email,
                    sha1_password: sha1(self.email + ':' + self.password)
                }, 
                method: "POST"
            }).done(function() {
                return location.assign('/');
            }).fail(function(xhr) {
                self.message = xhr.responseText;
                return $('.alert').show();
            });
        }
    }
})