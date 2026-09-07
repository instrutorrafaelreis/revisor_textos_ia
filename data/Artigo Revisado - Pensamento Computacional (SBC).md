# **O Pensamento Computacional como Ferramenta de Apoio ao Raciocínio Matemático**

**Rafael Filipe Vieira Reis**  
Serviço Nacional de Aprendizagem Industrial (SENAI MT)  
Cuiabá – MT – Brazil  
\[Seu e-mail aqui\]

**Abstract.** The transition from arithmetic thinking to algebraic abstraction poses significant cognitive challenges in Mathematics Education. Computational Thinking acts as a semiotic representation tool, allowing algebraic variables to be manipulated as memory variables in a script. Based on Seymour Papert's Constructionism and the taxonomy by Weintrop et al., this study investigates the relationship between algorithmic structures and mathematical reasoning. The paper explores the parametric decomposition and proposes modeling Monte Carlo simulations in Python for teaching Probability. We conclude that algorithm development provides a rigorous environment where Mathematical Logic becomes executable, enabling students to actively investigate hypotheses.

**Resumo.** A transição do pensamento aritmético para a abstração algébrica impõe desafios cognitivos significativos na Educação Matemática. O Pensamento Computacional (PC) atua como ferramenta de representação semiótica, permitindo que variáveis algébricas sejam manipuladas como variáveis de memória. Fundamentando-se no Construcionismo de Papert e na taxonomia de Weintrop et al., este artigo investiga a relação entre estruturas algorítmicas e o raciocínio matemático. O texto explora a decomposição paramétrica e propõe a modelagem de simulações de Monte Carlo em Python para o ensino de Probabilidade. Conclui-se que o desenvolvimento de algoritmos oferece um ambiente onde a Lógica Matemática se torna executável.

## **1\. Introdução**

A transição da aritmética para a álgebra exige a substituição do cálculo numérico específico pela generalização de estruturas. No contexto educacional, o Pensamento Computacional (PC) operacionaliza essa abstração; por exemplo, a generalização de uma soma manual pode ser codificada em Python por meio de um laço for i in range(n):, onde a variável *n* assume o papel do componente algébrico manipulável.  
Em vez de confinar o uso do computador à interação passiva com simulações no formato caixa-preta, a aproximação entre Matemática e Computação exige que o aprendiz atue como projetista do modelo lógico. Essa premissa fundamenta-se no Construcionismo de Seymour Papert, que postula que a aprendizagem matemática ocorre quando o estudante utiliza a linguagem de programação para construir artefatos computáveis, externalizando e depurando seu próprio raciocínio. Autores como \[Weintrop et al. 2016\] oferecem uma taxonomia especificamente voltada para as disciplinas de Matemática e Ciências. É no eixo das Práticas de Modelagem e Simulação propostas por \[Weintrop et al. 2016\] que este trabalho se ancora, demonstrando como a estruturação de simulações encontra paralelos com os conectivos e as proposições da Lógica Matemática.  
Para materializar essa proposta metodológica, este artigo adota um escopo empírico-aplicado: a exploração de simulações do método de Monte Carlo, desenvolvidas em linguagem Python, voltadas ao ensino prático de Probabilidade. A escolha dessa linguagem e deste objeto matemático ilustra de maneira tangível como o desenvolvimento de scripts exige do estudante a decomposição meticulosa de variáveis estocásticas e a formalização do espaço amostral.

## **2\. Fundamentação Teórica**

### **2.1. Aprofundamento epistemológico: abstração e decomposição matemática**

O Pensamento Computacional não se reduz à tradução de fórmulas matemáticas para linhas de código; ele exige a desconstrução estrutural do problema. A decomposição e a abstração, pilares do PC, adquirem contornos altamente específicos quando aplicados ao raciocínio lógico-matemático.  
A decomposição, sob a ótica matemática, vai muito além da simples divisão de tarefas. Ao resolver um problema de geometria espacial — como o cálculo de volume de sólidos irregulares pelo método de fatiamento —, a decomposição algorítmica exige que o estudante identifique os parâmetros invariáveis e os separe das variáveis iterativas. O aluno precisa fracionar o volume total em discos de espessura infinitesimal (aproximando-se intuitivamente do Cálculo Integral), estruturar um laço de repetição e consolidar os resultados em uma variável acumuladora. Essa exigência força a explicitação do raciocínio espacial em etapas executáveis estritas.  
Paralelamente, a abstração computacional atua como um degrau direto para a abstração algébrica. Na programação, ao generalizar um valor numérico fixo transformando-o em uma variável paramétrica ou em uma função modular, o estudante vivencia exatamente a mesma transição cognitiva necessária para compreender o papel de *x* ou *f(x)* na Álgebra. Ao desenvolver um algoritmo em Python para gerar distribuições estatísticas, por exemplo, o estudante constata que os mesmos parâmetros lógicos que regem o sorteio de cartas de um baralho podem ser abstraídos para prever a probabilidade de eventos complexos. O computador não resolve o problema pelo aluno; ele exige que o aluno seja preciso e semanticamente correto na formulação das regras, promovendo um nível de rigor lógico audível de forma imediata.

### **2.2. Pensamento matemático, modelagem e construcionismo**

A exigência de transformar ideias matemáticas em código executável requer clareza operacional que não permite ambiguidades. Diferente da resolução no papel, onde saltos lógicos podem ser ofuscados ou ignorados, o ambiente de desenvolvimento acusa falhas na estruturação do raciocínio. A relação entre a programação e a modelagem matemática foi corroborada por \[Ng and Cui 2021\], que observaram como a criação de algoritmos impulsiona a utilização de variáveis e promove ciclos contínuos de avaliação do próprio pensamento.  
Esse fenômeno é a base do Construcionismo. Para \[Papert 1980\], a tecnologia educacional atinge seu ápice quando o estudante ensina a máquina a pensar. Ao programar, o estudante está arquitetando seu próprio modelo cognitivo, validando axiomas matemáticos através da mecânica do código. Essa abordagem muda o foco da obtenção da resposta correta para a arquitetura do processo que gera a resposta.

## **3\. Metodologia**

Este estudo caracteriza-se como uma pesquisa bibliográfica exploratória de abordagem qualitativa, fundamentada na revisão crítica da literatura sobre Educação Matemática e Pensamento Computacional. A análise transcende as definições clássicas, incorporando as taxonomias propostas por \[Weintrop et al. 2016\] e a fundamentação epistemológica do Construcionismo.  
Como diferencial metodológico, este trabalho articula a teoria educacional com a engenharia de software aplicada à sala de aula, propondo um escopo empírico baseado no desenvolvimento de simulações matemáticas em Python. Essa escolha se justifica pela legibilidade da sintaxe de Python e por sua aderência aos princípios matemáticos de estruturação algorítmica, permitindo materializar conceitos teóricos — especificamente o ensino de Probabilidade via simulação de Monte Carlo — em artefatos testáveis e auditáveis.

## **4\. Aplicações Pedagógicas**

### **4.1. Aprendizagem baseada em problemas (ABP) na lógica algorítmica**

A integração do PC exige que a atividade didática migre da exposição passiva para o protagonismo estruturado. Ao adotar a Aprendizagem Baseada em Problemas (ABP), o professor instiga os estudantes a desenvolver algoritmos para solucionar desafios abertos, como a otimização de rotas ou modelagem financeira. Conforme argumentado por \[Rezende and Silva-Salse 2021\], a ABP é central para o pensamento crítico, e, quando aliada ao PC, transforma a matemática de uma disciplina de verificação em uma ciência de investigação e design.

### **4.2. Simulações computacionais e probabilidade: o método de Monte Carlo**

A Probabilidade é historicamente um dos ramos matemáticos mais beneficiados pela capacidade computacional. Em vez de limitar o aprendizado a fórmulas combinatórias descontextualizadas, o estudante deve atuar como criador do modelo estocástico. \[Wilensky 1995\] defende que construir modelos computacionais é a principal forma de dar sentido a conceitos como aleatoriedade e Lei dos Grandes Números.  
Uma das aplicações mais robustas desse conceito é a implementação do Método de Monte Carlo. Ao programar uma simulação em Python para calcular uma aproximação de Pi através do lançamento de pontos aleatórios em um plano cartesiano, o aluno vivencia a união entre geometria analítica e estatística inferencial.

import random

def aproximar\_pi\_monte\_carlo(pontos\_totais):  
    pontos\_no\_circulo \= 0  
      
    for \_ in range(pontos\_totais):  
        x \= random.uniform(0, 1\)  
        y \= random.uniform(0, 1\)  
          
        \# Teorema de Pitágoras: equação do círculo (x² \+ y² \<= r²)  
        distancia \= x\*\*2 \+ y\*\*2  
        if distancia \<= 1:  
            pontos\_no\_circulo \+= 1  
              
    \# Probabilidade (Área do Círculo / Área do Quadrado)  
    pi\_aproximado \= 4 \* pontos\_no\_circulo / pontos\_totais  
    return pi\_aproximado

resultado \= aproximar\_pi\_monte\_carlo(1000000)  
print(f"Aproximação matemática de Pi: {resultado}")

Neste código, a compreensão do Teorema de Pitágoras e a proporção geométrica de áreas é a espinha dorsal do algoritmo. A máquina atua apenas como o executor veloz; o intelecto matemático reside no design da função, materializando o cruzamento entre Álgebra e Probabilidade.

### **4.3. Depuração (debugging) como epistemologia do erro**

A depuração ou *debugging* afasta a ideia punitiva do erro matemático e o reposiciona como uma etapa científica de refinamento de hipóteses. Quando o resultado de uma função diverge do esperado, o estudante é provocado a investigar a hierarquia de operadores, as condições lógicas e os tipos de dados. Esse processo audita o raciocínio matemático passo a passo. A correção do *bug* exige reflexão: o erro é sintático (um parêntese esquecido) ou semântico (uma falha na própria equação formulada)?

## **5\. Resultados e Impactos Esperados**

A transição para um modelo educacional mediado pelo Pensamento Computacional gera impactos quantificáveis e qualitativos na apreensão da matemática. Para sistematizar essa evolução, a tabela abaixo evidencia as diferenças paradigmáticas entre a abordagem tradicional e a instrução orientada ao PC.

**Tabela 1\. Diferenças paradigmáticas entre a abordagem tradicional e a instrução orientada ao PC**

| Dimensão Cognitiva | Ensino Matemático Tradicional | Abordagem Apoiada pelo PC   |
| :---- | :---- | :---- |
| **Tratamento de Problemas** | Foco na busca pela fórmula correta e substituição de valores. | Foco na decomposição sistêmica, modelagem iterativa e abstrações paramétricas. |
| **Status do Erro** | Visto como fracasso cognitivo; resulta em dedução de notas. | Visto como evento de depuração (*debugging*); exige auditoria do modelo. |
| **Escalabilidade de Dados** | Limitada a amostras muito pequenas, dificultando visualizações. | Capacidade de iterar milhões de ciclos (ex: método de Monte Carlo). |

## **6\. Considerações Finais**

O Pensamento Computacional atua como muito mais do que um mero recurso utilitário para automatizar contas. Ele se consolida como uma infraestrutura de pensamento que viabiliza a execução da Lógica Matemática. A criação, manipulação e depuração de código oferecem um ambiente científico de experimentação no qual as abstrações matemáticas ganham materialidade estrutural. Como demonstrado através da aplicação de simulações estocásticas em Python e apoiado pela taxonomia de \[Weintrop et al. 2016\], a verdadeira disrupção metodológica reside em elevar o estudante à categoria de construtor do modelo cognitivo, substituindo o consumo de dogmas matemáticos pelo design algorítmico rigoroso.

## **Referências**

BARCELOS, Thiago; MUÑOZ, Roberto; ACEVEDO, Rodolfo Villarroel; SILVEIRA, Ismar Frango (2015). Relações entre o Pensamento Computacional e a Matemática: uma revisão sistemática da literatura. In: WORKSHOPS DO CONGRESSO BRASILEIRO DE INFORMÁTICA NA EDUCAÇÃO, 4., 2015, Maceió. Anais \[...\]. Porto Alegre: Sociedade Brasileira de Computação, p. 1369-1378.

BRASIL. Ministério da Educação (2018). Base Nacional Comum Curricular. Brasília, DF: MEC.

CHAN, Shiau-Wei; LOOI, Chee-Kit; HO, Weng Kin; KIM, Mi Song et al (2022). Tools and approaches for integrating computational thinking and mathematics: a scoping review of current empirical studies. Journal of Educational Computing Research, v. 60, n. 8, p. 2036-2080.

NG, Oi-Lam; CUI, Zhihao (2021). Examining primary students’ mathematical problem-solving in a programming context: towards computationally enhanced mathematics education. ZDM – Mathematics Education, v. 53, p. 847-860.

PAPERT, Seymour (1980). Mindstorms: children, computers, and powerful ideas. New York: Basic Books.

REZENDE, Adriano Alves de; SILVA-SALSE, Angela Ruth (2021). Utilização da aprendizagem baseada em problemas (ABP) para o desenvolvimento do pensamento crítico (PC) em Matemática: uma revisão teórica. Educação Matemática Debate, v. 5, n. 11, p. 1-21.

WEINTROP, David; BEHESHTI, Elham; HORN, Michael; ORTON, Kai; JUGO, Kemi; TROUT, Jason; WILENSKY, Uri (2016). Defining Computational Thinking for Mathematics and Science Classrooms. Journal of Science Education and Technology, v. 25, n. 1, p. 127-147.

WILENSKY, Uri (1995). Learning probability through building computational models. In: INTERNATIONAL CONFERENCE ON THE PSYCHOLOGY OF MATHEMATICS EDUCATION, 19., Recife. Proceedings \[...\]. Recife: PME.

WING, Jeannette M. (2006). Computational thinking. Communications of the ACM, v. 49, n. 3, p. 33-35.

WISNIEWSKI, Benedikt; ZIERER, Klaus; HATTIE, John (2020). The power of feedback revisited: a meta-analysis of educational feedback research. Frontiers in Psychology, v. 10, art. 3087, p. 1-14.