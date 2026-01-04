from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q
from django.db.models.deletion import ProtectedError, RestrictedError
from django.core.paginator import Paginator
from .models import Register, PessoaFisica, PessoaJuridica
from .forms import Detail_ModelForm, Pf_ModelForm, Pj_ModelForm


# =============================================================================================================
# PESSOA FISICA
# =============================================================================================================
class Pf_ListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    paginate_by = 10
    model = PessoaFisica
    template_name = 'register/list_person.html'
    permission_required = 'register.view_pessoafisica'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(cpf__icontains=query) | Q(last_name__icontains=query)
            )
        return queryset.order_by('name', 'last_name')


class Pf_DetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = PessoaFisica
    template_name = 'register/register_person.html'
    context_object_name = 'item'
    permission_required = 'register.view_pessoafisica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['form'] = Detail_ModelForm(instance=obj)
        context["is_detail"] = True
        return context


class Pf_CreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = PessoaFisica
    form_class = Pf_ModelForm
    template_name = 'register/register_person.html'
    success_url = reverse_lazy('register:person_')
    permission_required = 'register.add_pessoafisica'

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        try:
            url = super().form_valid(form)
        except IntegrityError as e:
            return self.handle_unique(e)

        messages.success(self.request, "Registro salvo com sucesso.")
        return url

    def handle_unique(self, e):
        if "cpf" in str(e):
            messages.warning(self.request, "Cadastro com CPF Duplicado. o registro nao foi salvo")
        else:
            messages.error(self.request, f"Erro. Salvamento cancelado {e}")
        return self.form_invalid(self.get_form())


class Pf_UpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = PessoaFisica
    form_class = Pf_ModelForm
    template_name = 'register/register_person.html'
    success_url = reverse_lazy('register:person_')
    permission_required = 'register.change_pessoafisica'

    def form_valid(self, form):

        try:
            url = super().form_valid(form)
        except IntegrityError as e:
            return self.handle_unique(e)

        messages.success(self.request, "Registro salvo com sucesso.")
        return url

    def handle_unique(self, e):
        if "cpf" in str(e):
            messages.warning(self.request, "Cadastro com CPF Duplicado. o registro nao foi salvo")
        else:
            messages.error(self.request, "Erro. Salvamento cancelado")
        return self.form_invalid(self.get_form())


class Pf_DeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    success_url = reverse_lazy("register:person_")
    permission_required = 'register.delete_pessoafisica'

    def post(self, request, pk, *args, **kwargs):
        registro = get_object_or_404(Register, id=pk)
        try:
            registro.delete()
            messages.success(request, "Cadastro deletado")
        except ProtectedError:
            messages.warning(request, "Não é possível deletar este registro pois existem outros dados vinculados.")
        except RestrictedError:
            messages.warning(request, "Não é possível deletar este registro devido a vínculos restritos.")
        except Exception:
            messages.error(request, "Ocorreu um erro ao tentar deletar este registro.")
        return redirect(self.success_url)


# =============================================================================================================
# EMPRESA
# =============================================================================================================
class Pj_ListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    paginate_by = 10
    model = PessoaJuridica
    template_name = 'register/list_enterprise.html'
    permission_required = 'register.view_pessoajuridica'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(fantasy__icontains=query) | Q(cnpj__icontains=query) | Q(legal__icontains=query)
            )
        return queryset.order_by('legal', 'fantasy')


class Pj_DetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = PessoaJuridica
    template_name = 'register/register_enterprise.html'
    context_object_name = 'item'
    permission_required = 'register.view_pessoajuridica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['form'] = Detail_ModelForm(instance=obj)
        context["is_detail"] = True
        return context


class Pj_CreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = PessoaJuridica
    form_class = Pj_ModelForm
    template_name = 'register/register_enterprise.html'
    success_url = reverse_lazy('register:enterprise_')
    permission_required = 'register.add_pessoajuridica'

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        try:
            url = super().form_valid(form)
        except IntegrityError as e:
            return self.handle_unique(e)

        messages.success(self.request, "Registro salvo com sucesso.")
        return url

    def handle_unique(self, e):
        if "cnpj" in str(e):
            messages.warning(self.request, "Cadastro com CNPJ duplicado. O registro não foi salvo.")
        else:
            messages.error(self.request, "Erro. Salvamento cancelado.")
        return self.form_invalid(self.get_form())


class Pj_UpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = PessoaJuridica
    form_class = Pj_ModelForm
    template_name = 'register/register_enterprise.html'
    success_url = reverse_lazy('register:enterprise_')
    permission_required = 'register.change_pessoajuridica'

    def form_valid(self, form):
        url = super().form_valid(form)
        messages.success(self.request, "Registro alterado com sucesso.")
        return url


class Pj_DeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    success_url = reverse_lazy("register:enterprise_")
    permission_required = 'register.delete_pessoajuridica'

    def post(self, request, pk, *args, **kwargs):
        registro = get_object_or_404(Register, id=pk)
        try:
            registro.delete()
            messages.success(request, "Cadastro deletado")
        except ProtectedError:
            messages.warning(request, "Não é possível deletar este registro pois existem outros dados vinculados.")
        except RestrictedError:
            messages.warning(request, "Não é possível deletar este registro devido a vínculos restritos.")
        except Exception:
            messages.error(request, "Ocorreu um erro ao tentar deletar este registro.")
        return redirect(self.success_url)


# =============================================================================================================
# LOGS
# =============================================================================================================
class Log_View(LoginRequiredMixin, PermissionRequiredMixin, View):
    paginate_by = 20
    template_name = "register/history.html"
    permission_required = 'register.view_register'

    def get(self, request, pk, *args, **kwargs):
        cadastro = get_object_or_404(Register, pk=pk)
        historico = list(cadastro.history.all().order_by("-history_date"))

        historico_com_diffs = []
        for i, item in enumerate(historico):
            diff_verbose = None
            if i + 1 < len(historico):
                previous = historico[i + 1]
                try:
                    diff_obj = item.diff_against(previous)
                    # Monta uma lista com verbose_name, old e new
                    diff_verbose = []
                    for change in diff_obj.changes:
                        field_name = change.field
                        try:
                            verbose_name = cadastro._meta.get_field(field_name).verbose_name
                        except Exception:
                            verbose_name = field_name  # fallback caso o campo não exista mais
                        diff_verbose.append({
                            "field": field_name,
                            "verbose_name": verbose_name,
                            "old": change.old,
                            "new": change.new,
                        })
                except AttributeError:
                    diff_verbose = None

            historico_com_diffs.append({"item": item, "diff": diff_verbose})

        paginator = Paginator(historico_com_diffs, self.paginate_by)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            self.template_name,
            {"cadastro": cadastro, "page_obj": page_obj})


class Pf_Log_View(LoginRequiredMixin, PermissionRequiredMixin, View):
    paginate_by = 20
    template_name = "register/history.html"
    permission_required = 'register.view_pessoafisica'

    def get(self, request, pk, *args, **kwargs):
        cadastro = get_object_or_404(PessoaFisica, pk=pk)
        historico = list(cadastro.history.all().order_by("-history_date"))

        historico_com_diffs = []
        for i, item in enumerate(historico):
            diff_verbose = None
            if i + 1 < len(historico):
                previous = historico[i + 1]
                try:
                    diff_obj = item.diff_against(previous)
                    # Monta uma lista com verbose_name, old e new
                    diff_verbose = []
                    for change in diff_obj.changes:
                        field_name = change.field
                        try:
                            verbose_name = cadastro._meta.get_field(field_name).verbose_name
                        except Exception:
                            verbose_name = field_name  # fallback caso o campo não exista mais
                        diff_verbose.append({
                            "field": field_name,
                            "verbose_name": verbose_name,
                            "old": change.old,
                            "new": change.new,
                        })
                except AttributeError:
                    diff_verbose = None

            historico_com_diffs.append({"item": item, "diff": diff_verbose})

        paginator = Paginator(historico_com_diffs, self.paginate_by)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            self.template_name,
            {"cadastro": cadastro, "page_obj": page_obj})


class Pj_Log_View(LoginRequiredMixin, PermissionRequiredMixin, View):
    paginate_by = 20
    template_name = "register/history.html"
    permission_required = 'register.view_pessoajuridica'

    def get(self, request, pk, *args, **kwargs):
        cadastro = get_object_or_404(PessoaJuridica, pk=pk)
        historico = list(cadastro.history.all().order_by("-history_date"))

        historico_com_diffs = []
        for i, item in enumerate(historico):
            diff_verbose = None
            if i + 1 < len(historico):
                previous = historico[i + 1]
                try:
                    diff_obj = item.diff_against(previous)
                    # Monta uma lista com verbose_name, old e new
                    diff_verbose = []
                    for change in diff_obj.changes:
                        field_name = change.field
                        try:
                            verbose_name = cadastro._meta.get_field(field_name).verbose_name
                        except Exception:
                            verbose_name = field_name  # fallback caso o campo não exista mais
                        diff_verbose.append({
                            "field": field_name,
                            "verbose_name": verbose_name,
                            "old": change.old,
                            "new": change.new,
                        })
                except AttributeError:
                    diff_verbose = None

            historico_com_diffs.append({"item": item, "diff": diff_verbose})

        paginator = Paginator(historico_com_diffs, self.paginate_by)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            self.template_name,
            {"cadastro": cadastro, "page_obj": page_obj})


# =============================================================================================================
# CONTATOS
# =============================================================================================================
class Contacts_ListView(LoginRequiredMixin, ListView):
    model = Register
    template_name = 'register/contacts.html'
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(last_name__icontains=query) | Q(legal__icontains=query) | Q(fantasy__icontains=query)
            )
        return queryset.order_by('fantasy', 'name')
