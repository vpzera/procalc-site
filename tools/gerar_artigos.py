import re, urllib.parse
import os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
home = open(D + 'index.html').read()
SYMBOL = re.search(r'<svg width="0".*?</svg>', home, re.S).group(0)
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Manrope:wght@400;500;600;700&display=swap">'
WA = 'https://wa.me/5581996324810?text='

def wa(msg):
    return WA + urllib.parse.quote(msg)

GTAG = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-11213439995"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-11213439995');
</script>

<!-- Conversão: Clique no WhatsApp (conta qualquer clique em link wa.me / WhatsApp) -->
<script>
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href*="wa.me"], a[href*="whatsapp.com"]');
    if (!link) return;
    var sendTo = 'AW-11213439995/UaNFCL_RgawdEPuH_uIp';
    if (link.target === '_blank') {
      gtag('event', 'conversion', { 'send_to': sendTo });
      return;
    }
    // Link que abre na mesma aba: espera o registro antes de sair da página
    e.preventDefault();
    var url = link.href, foi = false;
    function ir() { if (!foi) { foi = true; window.location.href = url; } }
    gtag('event', 'conversion', { 'send_to': sendTo, 'event_callback': ir });
    setTimeout(ir, 800);
  });
</script>'''

def page(title, desc, body, current):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
<link rel="stylesheet" href="blog.css">
{GTAG}
</head>
<body>
{SYMBOL}
<header>
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="Procalc Perícia Contábil, início">
      <img src="marca.png" alt="" width="138" height="106">
      <span class="brand-name"><b>PROCALC</b><small>Perícia Contábil</small></span>
    </a>
    <nav class="nav">
      <a class="link" href="artigos.html"{' aria-current="page"' if current else ''}>Artigos</a>
      <a class="btn btn-wa" href="{wa('Olá, vim pelo site e quero um orçamento')}" target="_blank" rel="noopener"><svg><use href="#wa"/></svg><span>Pedir orçamento</span></a>
    </nav>
  </div>
</header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap"><span>Procalc Perícia Contábil · Victor Pontes, CRC-PE 032.652</span><span><a href="index.html">Início</a> · <a href="artigos.html">Artigos</a></span></div></footer>
</body>
</html>
'''

ARTS = [
 dict(slug='artigo-liquidacao-trabalhista', area='Trabalhista', svc='cálculo trabalhista',
  title='Liquidação de sentença trabalhista: como é feito o cálculo',
  desc='Entenda o que é a liquidação de sentença trabalhista, quais documentos são usados, como funcionam correção e juros e o prazo para impugnar os cálculos.',
  summary='O que entra na conta, quais documentos usar e o prazo para impugnar.',
  body='''
<p class="lede">Ganhar a ação trabalhista é só metade do caminho. A sentença diz <em>o que</em> é devido; a liquidação diz <em>quanto</em>. É nessa fase que um cálculo bem feito, ou mal feito, muda o valor que o trabalhador recebe ou que a empresa paga.</p>
<h2>O que é a liquidação</h2>
<p>Depois que a decisão transita em julgado, o processo passa à fase de liquidação, prevista no artigo 879 da CLT. Na maioria dos casos ela é feita <strong>por cálculos</strong>: as verbas deferidas na sentença são transformadas em valores, mês a mês, com correção monetária e juros.</p>
<h2>O que entra na conta</h2>
<ul>
<li>As verbas deferidas: horas extras, adicionais, diferenças salariais, verbas rescisórias e seus reflexos em 13º, férias + 1/3, aviso prévio e FGTS.</li>
<li>A base de cálculo de cada verba, conforme os contracheques e os parâmetros da sentença.</li>
<li>Correção monetária e juros pelos índices definidos pelo STF nas ADCs 58 e 59, observadas as mudanças da Lei 14.905/2024.</li>
<li>Descontos de contribuição previdenciária e imposto de renda, quando cabíveis.</li>
<li>Honorários advocatícios e periciais fixados no processo.</li>
</ul>
<h2>Documentos necessários</h2>
<p>Sentença e acórdãos, petição inicial, contracheques, cartões de ponto (quando há horas extras), extrato do FGTS e termo de rescisão. Quanto mais completos os documentos, mais preciso o cálculo e menor a chance de impugnação.</p>
<h2>Por que o PJe-Calc</h2>
<p>A Justiça do Trabalho adota o PJe-Calc como ferramenta padrão de cálculo. Apresentar a conta nesse sistema facilita a conferência pelo juízo e pela outra parte e reduz discussões sobre metodologia.</p>
<div class="box"><p><strong>Atenção ao prazo:</strong> quando o juiz abre vista dos cálculos, as partes têm prazo comum de 8 dias para impugná-los de forma fundamentada, indicando os itens e valores discordantes (art. 879, § 2º, da CLT). Perdido o prazo, a discussão fica muito mais difícil.</p></div>
<h2>Erros que mais vemos</h2>
<ul>
<li>Aplicar índices de correção e juros diferentes dos fixados pelo STF.</li>
<li>Calcular horas extras sem respeitar o divisor ou a jornada definidos na sentença.</li>
<li>Esquecer reflexos ou, ao contrário, aplicar reflexos não deferidos.</li>
<li>Somar juros sobre juros ou corrigir valores já atualizados.</li>
</ul>
'''),
 dict(slug='artigo-revisao-pasep', area='Revisional', svc='revisão do PASEP',
  title='Revisão do PASEP: quem tem direito e quais documentos pedir',
  desc='Servidores com saldo no PASEP podem ter direito a diferenças por desfalques e falta de rendimentos. Veja o que o STJ decidiu no Tema 1.150 e como é feito o cálculo.',
  summary='O que o STJ decidiu no Tema 1.150 e como o saldo é recalculado.',
  body='''
<p class="lede">Muitos servidores e ex-servidores que sacaram o PASEP receberam valores muito abaixo do esperado. Em vários casos, a diferença vem de saques indevidos ou da falta de aplicação dos rendimentos devidos na conta individual.</p>
<h2>Quem pode ter direito</h2>
<p>Servidores públicos civis e militares cadastrados no PASEP até 4 de outubro de 1988, data a partir da qual não houve mais novas distribuições de cotas para as contas individuais. Herdeiros de titulares falecidos também podem buscar a revisão.</p>
<h2>O que o STJ decidiu (Tema 1.150)</h2>
<p>No julgamento dos recursos repetitivos do Tema 1.150, em 2023, o STJ fixou três pontos importantes (<a href="https://www.migalhas.com.br/quentes/394846/bb-responde-por-saques-indevidos-e-ma-gestao-em-contas-do-pasep" target="_blank" rel="noopener">resumo no Migalhas</a>):</p>
<ul>
<li>O <strong>Banco do Brasil</strong> pode ser réu nas ações sobre saques indevidos, desfalques e falta de aplicação dos rendimentos nas contas do PASEP.</li>
<li>O prazo para pedir o ressarcimento é de <strong>10 anos</strong> (art. 205 do Código Civil).</li>
<li>Esse prazo começa a contar quando o titular <strong>toma ciência dos desfalques</strong>, normalmente ao obter os extratos da conta.</li>
</ul>
<h2>Quais documentos pedir ao Banco do Brasil</h2>
<ul>
<li>Extratos microfilmados da conta PASEP, desde a abertura.</li>
<li>Extratos analíticos posteriores, até o saque total.</li>
<li>Comprovante do saque e documento com o número de inscrição no PASEP.</li>
</ul>
<h2>Como é feito o cálculo</h2>
<p>O saldo é reconstituído ano a ano, desde o primeiro depósito, aplicando as conversões de moeda, a correção monetária e os rendimentos definidos para o fundo em cada exercício. O resultado é comparado com o que foi efetivamente pago no saque. A diferença, atualizada, é o valor a ser pedido na ação.</p>
<div class="box"><p><strong>Antes de entrar com a ação:</strong> um cálculo extrajudicial mostra se a diferença compensa o processo e já serve de base para a petição inicial.</p></div>
'''),
 dict(slug='artigo-conferir-rescisao', area='Extrajudicial', svc='conferência de rescisão (extrajudicial)',
  title='Rescisão trabalhista: como conferir se você recebeu o valor certo',
  desc='Saiba quais verbas entram na rescisão, o prazo de pagamento e quando vale fazer um cálculo extrajudicial antes de entrar com uma ação trabalhista.',
  summary='Verbas, prazos e quando vale um cálculo antes de entrar com a ação.',
  body='''
<p class="lede">Recebeu a rescisão e ficou com dúvida sobre o valor? Um cálculo feito antes de qualquer processo mostra se há diferença a cobrar e quanto ela vale, para você decidir com números.</p>
<h2>Verbas que costumam entrar na rescisão sem justa causa</h2>
<ul>
<li>Saldo de salário dos dias trabalhados no mês.</li>
<li>Aviso prévio: 30 dias, mais 3 dias por ano completo de trabalho, até o limite de 90 dias (Lei 12.506/2011).</li>
<li>13º salário proporcional.</li>
<li>Férias vencidas e proporcionais, com o adicional de 1/3.</li>
<li>Multa de 40% sobre o saldo do FGTS e liberação do saque.</li>
</ul>
<p>Pedido de demissão, acordo entre as partes e justa causa mudam essa lista. Por isso o primeiro passo é saber exatamente qual foi o tipo de desligamento.</p>
<h2>Prazo de pagamento</h2>
<p>As verbas rescisórias devem ser pagas em até 10 dias após o fim do contrato (art. 477, § 6º, da CLT). O atraso gera multa equivalente a um salário do empregado (art. 477, § 8º).</p>
<h2>Onde costumam estar as diferenças</h2>
<ul>
<li>Horas extras, adicional noturno, insalubridade ou periculosidade que não entraram na média das verbas.</li>
<li>Aviso prévio calculado sem a proporcionalidade por tempo de serviço.</li>
<li>Depósitos de FGTS faltando durante o contrato, o que reduz também a multa de 40%.</li>
<li>Comissões e gratificações habituais fora da base de cálculo.</li>
</ul>
<div class="box"><p><strong>Fique atento ao prazo:</strong> a ação trabalhista deve ser proposta em até 2 anos após o fim do contrato e alcança os últimos 5 anos de trabalho (art. 7º, XXIX, da Constituição).</p></div>
<h2>Como funciona o cálculo extrajudicial</h2>
<p>Você envia o termo de rescisão, os contracheques e o extrato do FGTS. O cálculo compara o que foi pago com o que seria devido e aponta cada diferença, já atualizada. Com ele, você ou seu advogado decidem se vale negociar, ajuizar ou encerrar o assunto.</p>
'''),
]

for a in ARTS:
    body = f'''<article class="article">
<a class="back" href="artigos.html">← Todos os artigos</a>
<p class="area" style="margin-top:20px">{a['area']}</p>
<h1>{a['title']}</h1>
<p class="byline">Por Victor Pontes, contador CRC-PE 032.652 · 25 de outubro de 2026</p>
{a['body']}
<div class="cta">
<h2>Precisa desse cálculo?</h2>
<p>Envie os documentos pelo WhatsApp e receba o orçamento.</p>
<a class="btn btn-wa" href="{wa('Li o artigo no site e quero orçamento de ' + a['svc'])}" target="_blank" rel="noopener"><svg><use href="#wa"/></svg>Pedir orçamento no WhatsApp</a>
</div>
<p class="disclaimer">Conteúdo informativo. Não substitui a análise do seu caso por um advogado ou contador.</p>
</article>'''
    open(D + a['slug'] + '.html', 'w').write(page(a['title'] + ' | Procalc', a['desc'], body, False))

cards = '\n'.join(f'''<a class="post" href="{a['slug']}.html"><span class="area">{a['area']}</span><h2>{a['title']}</h2><p>{a['summary']}</p><span class="more">Ler artigo →</span></a>''' for a in ARTS)
idx = f'''<div class="blog-head"><p class="kicker">Artigos</p><h1>Cálculos, perícia e direito, explicados</h1><p>Conteúdo para advogados e clientes entenderem cada tipo de cálculo antes de contratar.</p></div>
<div class="posts">{cards}</div>'''
open(D + 'artigos.html', 'w').write(page('Artigos | Procalc Perícia Contábil', 'Artigos sobre cálculos judiciais e extrajudiciais, perícia contábil e direito.', idx, True))
print('ok')
