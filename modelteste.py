# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthAcesso(models.Model):
    addseparator = models.TextField(db_column='addSeparator')  # Field name made lowercase. This field type is a guess.
    icone = models.CharField(max_length=255, blank=True, null=True)
    nomemenu = models.CharField(db_column='nomeMenu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ordem = models.SmallIntegerField()
    path = models.CharField(max_length=256, blank=True, null=True)
    titulopagina = models.CharField(db_column='tituloPagina', max_length=100, blank=True, null=True)  # Field name made lowercase.
    menupai = models.ForeignKey('self', models.DO_NOTHING, db_column='menuPai_id', blank=True, null=True)  # Field name made lowercase.
    ocultarnomenu = models.TextField(db_column='ocultarNoMenu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_acesso'


class AuthConfiguracao(models.Model):
    chave = models.CharField(primary_key=True, max_length=100)
    valor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_configuracao'


class AuthEndPoint(models.Model):
    antpattern = models.CharField(db_column='antPattern', max_length=255, blank=True, null=True)  # Field name made lowercase.
    api = models.TextField()  # This field type is a guess.
    httpmethod = models.CharField(db_column='httpMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_end_point'


class AuthFoto(models.Model):
    contenttype = models.CharField(db_column='contentType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stream = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_foto'


class AuthIconeDashboard(models.Model):
    contenttype = models.CharField(db_column='contentType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stream = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_icone_dashboard'


class AuthMenuItem(models.Model):
    icone = models.CharField(max_length=150, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    ocultar = models.TextField()  # This field type is a guess.
    ordem = models.SmallIntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)
    menu_pai = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    icone_dashboard = models.ForeignKey(AuthIconeDashboard, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_menu_item'


class AuthPerfil(models.Model):
    nome = models.CharField(primary_key=True, max_length=100)
    perfil_pai = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_perfil'


class AuthPerfilAcesso(models.Model):
    perfil = models.OneToOneField(AuthPerfil, models.DO_NOTHING, primary_key=True)  # The composite primary key (perfil_id, acesso_id) found, that is not supported. The first column is selected.
    acesso = models.ForeignKey(AuthAcesso, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_perfil_acesso'
        unique_together = (('perfil', 'acesso'),)


class AuthPerfilEndPoint(models.Model):
    perfil = models.ForeignKey(AuthPerfil, models.DO_NOTHING)
    end_point = models.ForeignKey(AuthEndPoint, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_perfil_end_point'


class AuthPerfilMenuItem(models.Model):
    perfil = models.OneToOneField(AuthPerfil, models.DO_NOTHING, primary_key=True)  # The composite primary key (perfil_id, menu_item_id) found, that is not supported. The first column is selected.
    menu_item = models.ForeignKey(AuthMenuItem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_perfil_menu_item'
        unique_together = (('perfil', 'menu_item'),)


class AuthUsuario(models.Model):
    matricula = models.CharField(primary_key=True, max_length=100)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    foto = models.ForeignKey(AuthFoto, models.DO_NOTHING, blank=True, null=True)
    apelido = models.CharField(max_length=50, blank=True, null=True)
    tipoautenticacao = models.CharField(db_column='tipoAutenticacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=14, blank=True, null=True)
    desativado = models.TextField()  # This field type is a guess.
    usuarioexterno = models.TextField(db_column='usuarioExterno', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    digital = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_usuario'


class AuthUsuarioPerfil(models.Model):
    usuario = models.OneToOneField(AuthUsuario, models.DO_NOTHING, primary_key=True)  # The composite primary key (usuario_id, perfil_id) found, that is not supported. The first column is selected.
    perfil = models.ForeignKey(AuthPerfil, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_usuario_perfil'
        unique_together = (('usuario', 'perfil'),)


class CafAnimal(models.Model):
    datanascimento = models.DateField(db_column='dataNascimento', blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(max_length=255, blank=True, null=True)
    identificacao = models.CharField(unique=True, max_length=55)
    outraprocedencia = models.CharField(db_column='outraProcedencia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    padraoracial = models.CharField(db_column='padraoRacial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    procedencia = models.CharField(max_length=255, blank=True, null=True)
    sexo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caf_animal'


class CafAtividadeEscalaTrabalho(models.Model):
    avaliacao = models.CharField(max_length=30, blank=True, null=True)
    datahoraregistroavaliacao = models.DateTimeField(db_column='dataHoraRegistroAvaliacao', blank=True, null=True)  # Field name made lowercase.
    datahoraregistrosituacao = models.DateTimeField(db_column='dataHoraRegistroSituacao', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=255, blank=True, null=True)
    local = models.CharField(max_length=255, blank=True, null=True)
    observacaoavaliacao = models.CharField(db_column='observacaoAvaliacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    observacaosituacao = models.CharField(db_column='observacaoSituacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ordem = models.IntegerField()
    situacao = models.CharField(max_length=30, blank=True, null=True)
    escala = models.ForeignKey('CafEscalaTrabalho', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caf_atividade_escala_trabalho'


class CafEscalaTrabalho(models.Model):
    datafim = models.DateField(db_column='dataFim', blank=True, null=True)  # Field name made lowercase.
    datainicio = models.DateField(db_column='dataInicio', blank=True, null=True)  # Field name made lowercase.
    dataultimaalteracaostatus = models.DateTimeField(db_column='dataUltimaAlteracaoStatus', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=30, blank=True, null=True)
    tecnico_responsavel_id = models.CharField(max_length=100, blank=True, null=True)
    trabalhador_caf_id = models.CharField(max_length=100, blank=True, null=True)
    usuario_ultima_alteracao_status_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caf_escala_trabalho'


class CafExameClinico(models.Model):
    achadosclinicoscirculatorio = models.CharField(db_column='achadosClinicosCirculatorio', max_length=150, blank=True, null=True)  # Field name made lowercase.
    achadosclinicosdigestivo = models.CharField(db_column='achadosClinicosDigestivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    achadosclinicosgenitourinario = models.CharField(db_column='achadosClinicosGenitoUrinario', max_length=150, blank=True, null=True)  # Field name made lowercase.
    achadosclinicoslinfatico = models.CharField(db_column='achadosClinicosLinfatico', max_length=150, blank=True, null=True)  # Field name made lowercase.
    achadosclinicosnervoso = models.CharField(db_column='achadosClinicosNervoso', max_length=150, blank=True, null=True)  # Field name made lowercase.
    achadosclinicosoutros = models.CharField(db_column='achadosClinicosOutros', max_length=150, blank=True, null=True)  # Field name made lowercase.
    achadosclinicosrespiratorio = models.CharField(db_column='achadosClinicosRespiratorio', max_length=150, blank=True, null=True)  # Field name made lowercase.
    conclusaoexamescomplementares = models.CharField(db_column='conclusaoExamesComplementares', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conclusaoprognostico = models.CharField(db_column='conclusaoPrognostico', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conclusaosuspeitadiagnostico = models.CharField(db_column='conclusaoSuspeitaDiagnostico', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conclusaotratamento = models.CharField(db_column='conclusaoTratamento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datahoradacadastro = models.DateTimeField(db_column='dataHoraDaCadastro', blank=True, null=True)  # Field name made lowercase.
    estadogeral = models.CharField(db_column='estadoGeral', max_length=150, blank=True, null=True)  # Field name made lowercase.
    mucosas = models.CharField(max_length=150, blank=True, null=True)
    parametroar = models.CharField(db_column='parametroAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parametrod = models.CharField(db_column='parametroD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parametroecc = models.CharField(db_column='parametroECC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parametrofc = models.CharField(db_column='parametroFC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parametrofr = models.CharField(db_column='parametroFR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parametrotc = models.CharField(db_column='parametroTC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parametrotpv = models.CharField(db_column='parametroTPV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    veterinario = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caf_exame_clinico'


class CafSolicitacaoAtendimentoVeterinario(models.Model):
    anamnese = models.CharField(max_length=255, blank=True, null=True)
    datahoradasolicitacao = models.DateTimeField(db_column='dataHoraDaSolicitacao', blank=True, null=True)  # Field name made lowercase.
    dataultimavacinacao = models.DateField(db_column='dataUltimaVacinacao', blank=True, null=True)  # Field name made lowercase.
    dataultimavermifugacao = models.DateField(db_column='dataUltimaVermifugacao', blank=True, null=True)  # Field name made lowercase.
    outroatendimento = models.CharField(db_column='outroAtendimento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quaisvacinas = models.CharField(db_column='quaisVacinas', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quaisvermifugos = models.CharField(db_column='quaisVermifugos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    tipoatendimento = models.CharField(db_column='tipoAtendimento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vacinado = models.TextField()  # This field type is a guess.
    vermifugado = models.TextField()  # This field type is a guess.
    animal = models.ForeignKey(CafAnimal, models.DO_NOTHING, blank=True, null=True)
    exame_clinico = models.OneToOneField(CafExameClinico, models.DO_NOTHING, blank=True, null=True)
    solicitante_usuario = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caf_solicitacao_atendimento_veterinario'


class CafSolicitacaoAulaPratica(models.Model):
    assunto = models.CharField(max_length=1024, blank=True, null=True)
    disciplina = models.CharField(max_length=150, blank=True, null=True)
    justificativaindeferimento = models.CharField(db_column='justificativaIndeferimento', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    materiais = models.CharField(max_length=1024, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    professor_usuario = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)
    turma = models.ForeignKey('ChTurma', models.DO_NOTHING, blank=True, null=True)
    usuario_autorizacao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, related_name='cafsolicitacaoaulapratica_usuario_autorizacao_set', blank=True, null=True)
    datahoraautorizacao = models.DateTimeField(db_column='dataHoraAutorizacao', blank=True, null=True)  # Field name made lowercase.
    datahorasolicitacao = models.DateTimeField(db_column='dataHoraSolicitacao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caf_solicitacao_aula_pratica'


class CafSolicitacaoaulapraticaDiasaulapratica(models.Model):
    solicitacaoaulapratica = models.ForeignKey(CafSolicitacaoAulaPratica, models.DO_NOTHING, db_column='SolicitacaoAulaPratica_id')  # Field name made lowercase.
    diasaulapratica = models.DateTimeField(db_column='diasAulaPratica', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caf_solicitacaoaulapratica_diasaulapratica'


class CertAtividade(models.Model):
    cargahoraria = models.IntegerField(db_column='cargaHoraria')  # Field name made lowercase.
    datahoraultimaalteracao = models.DateTimeField(db_column='dataHoraUltimaAlteracao', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=255, blank=True, null=True)
    evento = models.ForeignKey('CertEvento', models.DO_NOTHING, blank=True, null=True)
    tipo_atividade = models.ForeignKey('CertTipoAtividade', models.DO_NOTHING, blank=True, null=True)
    usuario_ultima_alteracao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cert_atividade'


class CertCodigoCertificado(models.Model):
    codigo_certificado = models.CharField(primary_key=True, max_length=23)
    datahoraemissao = models.DateTimeField(db_column='dataHoraEmissao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cert_codigo_certificado'


class CertEvento(models.Model):
    cargahoraria = models.IntegerField(db_column='cargaHoraria', blank=True, null=True)  # Field name made lowercase.
    datahoraultimaalteracao = models.DateTimeField(db_column='dataHoraUltimaAlteracao', blank=True, null=True)  # Field name made lowercase.
    fimevento = models.DateField(db_column='fimEvento', blank=True, null=True)  # Field name made lowercase.
    inicioevento = models.DateField(db_column='inicioEvento', blank=True, null=True)  # Field name made lowercase.
    tema = models.CharField(max_length=255, blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    usuario_cadastro = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)
    usuario_ultima_alteracao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, related_name='certevento_usuario_ultima_alteracao_set', blank=True, null=True)
    imagem_fundo_certificado = models.ForeignKey('CertImagemFundoCertificado', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cert_evento'


class CertImagemFundoCertificado(models.Model):
    contenttype = models.CharField(db_column='contentType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stream = models.TextField(blank=True, null=True)
    fundodefault = models.TextField(db_column='fundoDefault', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cert_imagem_fundo_certificado'


class CertOrganizadorEvento(models.Model):
    evento = models.OneToOneField(CertEvento, models.DO_NOTHING, primary_key=True)  # The composite primary key (evento_id, organizador_id) found, that is not supported. The first column is selected.
    organizador = models.ForeignKey(AuthUsuario, models.DO_NOTHING)
    datahoraultimaalteracao = models.DateTimeField(db_column='dataHoraUltimaAlteracao', blank=True, null=True)  # Field name made lowercase.
    emailenviado = models.TextField(db_column='emailEnviado')  # Field name made lowercase. This field type is a guess.
    codigo_certificado = models.ForeignKey(CertCodigoCertificado, models.DO_NOTHING, db_column='codigo_certificado', blank=True, null=True)
    usuario_ultima_alteracao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, related_name='certorganizadorevento_usuario_ultima_alteracao_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cert_organizador_evento'
        unique_together = (('evento', 'organizador'),)


class CertParticipanteAtividade(models.Model):
    atividade = models.OneToOneField(CertAtividade, models.DO_NOTHING, primary_key=True)  # The composite primary key (atividade_id, participante_id) found, that is not supported. The first column is selected.
    participante = models.ForeignKey(AuthUsuario, models.DO_NOTHING)
    datahoraultimaalteracao = models.DateTimeField(db_column='dataHoraUltimaAlteracao', blank=True, null=True)  # Field name made lowercase.
    emailenviado = models.TextField(db_column='emailEnviado')  # Field name made lowercase. This field type is a guess.
    tipoparticipacao = models.CharField(db_column='tipoParticipacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigo_certificado = models.ForeignKey(CertCodigoCertificado, models.DO_NOTHING, db_column='codigo_certificado', blank=True, null=True)
    usuario_ultima_alteracao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, related_name='certparticipanteatividade_usuario_ultima_alteracao_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cert_participante_atividade'
        unique_together = (('atividade', 'participante'),)


class CertParticipanteEvento(models.Model):
    evento = models.OneToOneField(CertEvento, models.DO_NOTHING, primary_key=True)  # The composite primary key (evento_id, participante_id) found, that is not supported. The first column is selected.
    participante = models.ForeignKey(AuthUsuario, models.DO_NOTHING)
    datahoraultimaalteracao = models.DateTimeField(db_column='dataHoraUltimaAlteracao', blank=True, null=True)  # Field name made lowercase.
    emailenviado = models.TextField(db_column='emailEnviado')  # Field name made lowercase. This field type is a guess.
    emailfalhaenvio = models.TextField(db_column='emailFalhaEnvio')  # Field name made lowercase. This field type is a guess.
    codigo_certificado = models.ForeignKey(CertCodigoCertificado, models.DO_NOTHING, db_column='codigo_certificado', blank=True, null=True)
    usuario_ultima_alteracao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, related_name='certparticipanteevento_usuario_ultima_alteracao_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cert_participante_evento'
        unique_together = (('evento', 'participante'),)


class CertTipoAtividade(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cert_tipo_atividade'


class ChAfastamento(models.Model):
    dataalteracaostatus = models.DateTimeField(db_column='dataAlteracaoStatus', blank=True, null=True)  # Field name made lowercase.
    descricaomotivo = models.CharField(db_column='descricaoMotivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fim = models.DateField(blank=True, null=True)
    inicio = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    arquivo = models.ForeignKey('ChAnexoAfastamento', models.DO_NOTHING, blank=True, null=True)
    motivo_afastamento = models.ForeignKey('ChMotivoAfastamento', models.DO_NOTHING, blank=True, null=True)
    professor = models.ForeignKey('ChProfessor', models.DO_NOTHING, blank=True, null=True)
    usuario_alteracao_status = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_afastamento'


class ChAfastamentoHorarioAula(models.Model):
    afastamento_id = models.IntegerField(primary_key=True)  # The composite primary key (afastamento_id, horario_aula_id) found, that is not supported. The first column is selected.
    horario_aula_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ch_afastamento_horario_aula'
        unique_together = (('afastamento_id', 'horario_aula_id'),)


class ChAluno(models.Model):
    email2responsavel = models.CharField(db_column='email2Responsavel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailpessoal = models.CharField(db_column='emailPessoal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailresponsavel = models.CharField(db_column='emailResponsavel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nomeresponsavel = models.CharField(db_column='nomeResponsavel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefone2responsavel = models.CharField(db_column='telefone2Responsavel', max_length=30, blank=True, null=True)  # Field name made lowercase.
    telefoneresponsavel = models.CharField(db_column='telefoneResponsavel', max_length=30, blank=True, null=True)  # Field name made lowercase.
    matricula = models.OneToOneField(AuthUsuario, models.DO_NOTHING, db_column='matricula', primary_key=True)
    turma = models.ForeignKey('ChTurma', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_aluno'


class ChAlunoTelefones(models.Model):
    aluno_matricula = models.ForeignKey(ChAluno, models.DO_NOTHING, db_column='Aluno_matricula')  # Field name made lowercase.
    telefones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_aluno_telefones'


class ChAnexoAfastamento(models.Model):
    contenttype = models.CharField(db_column='contentType', max_length=155, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=155, blank=True, null=True)  # Field name made lowercase.
    stream = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_anexo_afastamento'


class ChCalendario(models.Model):
    ativo = models.TextField()  # This field type is a guess.
    inicio_das_aulas = models.DateField(blank=True, null=True)
    sigla = models.CharField(max_length=20, blank=True, null=True)
    termino_das_aulas = models.DateField(blank=True, null=True)
    tempohorario = models.IntegerField(db_column='tempoHorario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ch_calendario'


class ChChamada(models.Model):
    diadomes = models.DateField(db_column='diaDoMes', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ch_chamada'


class ChChamadaAluno(models.Model):
    chamadas_diadomes = models.OneToOneField(ChChamada, models.DO_NOTHING, db_column='chamadas_diaDoMes', primary_key=True)  # Field name made lowercase. The composite primary key (chamadas_diaDoMes, alunosAusentes_matricula) found, that is not supported. The first column is selected.
    alunosausentes_matricula = models.ForeignKey(ChAluno, models.DO_NOTHING, db_column='alunosAusentes_matricula')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ch_chamada_aluno'
        unique_together = (('chamadas_diadomes', 'alunosausentes_matricula'),)


class ChDisciplina(models.Model):
    anual = models.TextField()  # This field type is a guess.
    cargahoraria = models.IntegerField(db_column='cargaHoraria', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(max_length=128, blank=True, null=True)
    sigla = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_disciplina'


class ChDisciplinaTurma(models.Model):
    aulassincronasporsemana = models.IntegerField(db_column='aulasSincronasPorSemana', blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(max_length=255, blank=True, null=True)
    horariosporsemana = models.IntegerField(db_column='horariosPorSemana', blank=True, null=True)  # Field name made lowercase.
    disciplina = models.ForeignKey(ChDisciplina, models.DO_NOTHING)
    professor_atual = models.ForeignKey('ChProfessor', models.DO_NOTHING, blank=True, null=True)
    sala = models.ForeignKey('ChSala', models.DO_NOTHING, blank=True, null=True)
    turma = models.ForeignKey('ChTurma', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ch_disciplina_turma'


class ChFeriado(models.Model):
    data = models.DateField(unique=True, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_feriado'


class ChHorario(models.Model):
    fim = models.TimeField(blank=True, null=True)
    inicio = models.TimeField(blank=True, null=True)
    ordem = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_horario'


class ChHorarioAula(models.Model):
    diadasemanaenum = models.CharField(db_column='diaDaSemanaEnum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disciplina = models.ForeignKey(ChDisciplinaTurma, models.DO_NOTHING)
    horario = models.ForeignKey(ChHorario, models.DO_NOTHING)
    afastamento = models.ForeignKey(ChAfastamento, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_horario_aula'


class ChMotivoAfastamento(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)
    anexoobrigatorio = models.TextField(db_column='anexoObrigatorio')  # Field name made lowercase. This field type is a guess.
    descricaoobrigatoria = models.TextField(db_column='descricaoObrigatoria')  # Field name made lowercase. This field type is a guess.
    ocultar = models.TextField(blank=True, null=True)  # This field type is a guess.
    ordem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_motivo_afastamento'


class ChPermutaHorario(models.Model):
    datahoraultimaalteracao = models.DateTimeField(db_column='dataHoraUltimaAlteracao', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=30, blank=True, null=True)
    solicitante_matricula = models.ForeignKey('ChProfessor', models.DO_NOTHING, db_column='solicitante_matricula', blank=True, null=True)
    usuarioultimaalteracao_matricula = models.ForeignKey(AuthUsuario, models.DO_NOTHING, db_column='usuarioUltimaAlteracao_matricula', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ch_permuta_horario'


class ChProfessor(models.Model):
    matricula = models.OneToOneField(AuthUsuario, models.DO_NOTHING, db_column='matricula', primary_key=True)

    class Meta:
        managed = False
        db_table = 'ch_professor'


class ChRegistroAluno(models.Model):
    data_registro = models.DateTimeField(blank=True, null=True)
    diadomes = models.DateField(db_column='diaDoMes', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(max_length=255, blank=True, null=True)
    statusenum = models.CharField(db_column='statusEnum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aula_substituta = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    disciplina = models.ForeignKey(ChDisciplinaTurma, models.DO_NOTHING)
    horario = models.ForeignKey(ChHorario, models.DO_NOTHING)
    usuario = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)
    professor = models.ForeignKey(ChProfessor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_registro_aluno'


class ChRegistroAula(models.Model):
    data_registro = models.DateTimeField(blank=True, null=True)
    diadomes = models.DateField(db_column='diaDoMes', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(max_length=255, blank=True, null=True)
    statusenum = models.CharField(db_column='statusEnum', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aula_substituta = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    disciplina = models.ForeignKey(ChDisciplinaTurma, models.DO_NOTHING)
    horario = models.ForeignKey(ChHorario, models.DO_NOTHING)
    usuario = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)
    professor = models.ForeignKey(ChProfessor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_registro_aula'


class ChRegistroAulaExtra(models.Model):
    diadomes = models.DateField(db_column='diaDoMes', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(max_length=255, blank=True, null=True)
    statusenum = models.CharField(db_column='statusEnum', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aula_extra_substituta = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    professor = models.ForeignKey(ChProfessor, models.DO_NOTHING, blank=True, null=True)
    disciplina = models.ForeignKey(ChDisciplinaTurma, models.DO_NOTHING)
    horario = models.ForeignKey(ChHorario, models.DO_NOTHING)
    usuario = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)
    data_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_registro_aula_extra'


class ChSala(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)
    numero = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_sala'


class ChTurma(models.Model):
    abreviacao = models.CharField(max_length=20, blank=True, null=True)
    codigo_suap = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    serie = models.CharField(max_length=10, blank=True, null=True)
    turnoenum = models.CharField(db_column='turnoEnum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    matricula_assistente = models.ForeignKey(AuthUsuario, models.DO_NOTHING, db_column='matricula_assistente', blank=True, null=True)
    matricula_assistente2 = models.ForeignKey(AuthUsuario, models.DO_NOTHING, db_column='matricula_assistente2', related_name='chturma_matricula_assistente2_set', blank=True, null=True)
    calendario = models.ForeignKey(ChCalendario, models.DO_NOTHING, blank=True, null=True)
    matricula_coordenador = models.ForeignKey(ChProfessor, models.DO_NOTHING, db_column='matricula_coordenador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ch_turma'


class ChavesBloco(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)
    letra = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chaves_bloco'


class ChavesChave(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)
    letra = models.CharField(max_length=7, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bloco = models.ForeignKey(ChavesBloco, models.DO_NOTHING, blank=True, null=True)
    chavepublica = models.TextField(db_column='chavePublica', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'chaves_chave'


class ChavesEmprestimoChave(models.Model):
    datadevolucao = models.DateTimeField(db_column='dataDevolucao', blank=True, null=True)  # Field name made lowercase.
    dataemprestimo = models.DateTimeField(db_column='dataEmprestimo')  # Field name made lowercase.
    chave = models.ForeignKey(ChavesChave, models.DO_NOTHING, blank=True, null=True)
    usuario_devolucao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)
    usuario_emprestimo = models.ForeignKey(AuthUsuario, models.DO_NOTHING, related_name='chavesemprestimochave_usuario_emprestimo_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chaves_emprestimo_chave'


class ChavesEmprestimoEquipamento(models.Model):
    datadevolucao = models.DateTimeField(db_column='dataDevolucao', blank=True, null=True)  # Field name made lowercase.
    dataemprestimo = models.DateTimeField(db_column='dataEmprestimo')  # Field name made lowercase.
    equipamento = models.ForeignKey('ChavesEquipamento', models.DO_NOTHING, blank=True, null=True)
    usuario_devolucao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, blank=True, null=True)
    usuario_emprestimo = models.ForeignKey(AuthUsuario, models.DO_NOTHING, related_name='chavesemprestimoequipamento_usuario_emprestimo_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chaves_emprestimo_equipamento'


class ChavesEquipamento(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chaves_equipamento'


class ChavesResponsavelChave(models.Model):
    chave = models.OneToOneField(ChavesChave, models.DO_NOTHING, primary_key=True)  # The composite primary key (chave_id, responsavel_chave_id) found, that is not supported. The first column is selected.
    responsavel_chave = models.ForeignKey(AuthUsuario, models.DO_NOTHING)
    datahoraultimaalteracao = models.DateTimeField(db_column='dataHoraUltimaAlteracao', blank=True, null=True)  # Field name made lowercase.
    usuario_ultima_alteracao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, related_name='chavesresponsavelchave_usuario_ultima_alteracao_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chaves_responsavel_chave'
        unique_together = (('chave', 'responsavel_chave'),)


class ChavesUsuarioAutorizado(models.Model):
    chave = models.OneToOneField(ChavesChave, models.DO_NOTHING, primary_key=True)  # The composite primary key (chave_id, usuario_id) found, that is not supported. The first column is selected.
    usuario = models.ForeignKey(AuthUsuario, models.DO_NOTHING)
    datahoraautorizacao = models.DateTimeField(db_column='dataHoraAutorizacao', blank=True, null=True)  # Field name made lowercase.
    responsavel_autorizacao = models.ForeignKey(AuthUsuario, models.DO_NOTHING, related_name='chavesusuarioautorizado_responsavel_autorizacao_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chaves_usuario_autorizado'
        unique_together = (('chave', 'usuario'),)
