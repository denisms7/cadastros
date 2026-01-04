from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import PessoaFisica, PessoaJuridica


@admin.register(PessoaFisica)
class PessoaFisicaAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'name', 'last_name', 'cpf', 'birth', 'active', 'created_at')
    list_filter = ('active', 'sex', 'education', 'created_at')
    search_fields = ('name', 'last_name', 'cpf', 'rg')
    readonly_fields = ('created_at', 'created_by', 'type')

    fieldsets = (
        ('Dados Principais', {
            'fields': ('active', 'name', 'last_name', 'cpf', 'sex', 'birth', 'education')
        }),
        ('Documentos', {
            'fields': ('rg', 'rg_issuer', 'rg_expedition'),
        }),
        ('CNH', {
            'fields': ('cnh_n', 'cnh_emission', 'cnh_validity', 'cnh_category'),
            'classes': ('collapse',)
        }),
        ('Estado Civil e Família', {
            'fields': ('spouse_status', 'spouse_name', 'spouse_last_name', 'mother_name', 'mother_last_name', 'father_name', 'father_last_name'),
            'classes': ('collapse',)
        }),
        ('Contato', {
            'fields': ('email_1', 'email_2', 'phone_1', 'phone_1_type', 'phone_2', 'phone_2_type', 'phone_3', 'phone_3_type', 'link_1', 'link_2', 'obs_contact'),
            'classes': ('collapse',)
        }),
        ('Endereço', {
            'fields': ('cep', 'state', 'city', 'neighborhood', 'address', 'number', 'complement', 'obs_address'),
            'classes': ('collapse',)
        }),
        ('Dados Bancários', {
            'fields': ('title_holder', 'document_type', 'document_holder', 'account_type', 'bank', 'agency', 'account', 'digit', 'pix_1', 'pix_2', 'obs_bank'),
            'classes': ('collapse',)
        }),
        ('Observações', {
            'fields': ('obs',),
            'classes': ('collapse',)
        }),
        ('Sistema', {
            'fields': ('type', 'created_at', 'created_by'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=0)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.type = 0
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'legal', 'fantasy', 'cnpj', 'cnpj_situation', 'active', 'created_at')
    list_filter = ('active', 'cnpj_situation', 'cnpj_carrying', 'created_at')
    search_fields = ('legal', 'fantasy', 'cnpj')
    readonly_fields = ('created_at', 'created_by', 'type')

    fieldsets = (
        ('Dados Principais', {
            'fields': ('active', 'legal', 'fantasy', 'cnpj')
        }),
        ('Informações da Empresa', {
            'fields': ('cnpj_situation', 'cnpj_carrying', 'cnpj_date', 'cnpj_type_activity', 'cnpj_activity', 'n_state', 'n_municipal'),
        }),
        ('Contato', {
            'fields': ('email_1', 'email_2', 'phone_1', 'phone_1_type', 'phone_2', 'phone_2_type', 'phone_3', 'phone_3_type', 'link_1', 'link_2', 'obs_contact'),
            'classes': ('collapse',)
        }),
        ('Endereço', {
            'fields': ('cep', 'state', 'city', 'neighborhood', 'address', 'number', 'complement', 'obs_address'),
            'classes': ('collapse',)
        }),
        ('Dados Bancários', {
            'fields': ('title_holder', 'document_type', 'document_holder', 'account_type', 'bank', 'agency', 'account', 'digit', 'pix_1', 'pix_2', 'obs_bank'),
            'classes': ('collapse',)
        }),
        ('Observações', {
            'fields': ('obs',),
            'classes': ('collapse',)
        }),
        ('Sistema', {
            'fields': ('type', 'created_at', 'created_by'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=1)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.type = 1
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
