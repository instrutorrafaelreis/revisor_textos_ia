# **O Pensamento Computacional como Ferramenta de Apoio ao Raciocínio Matemático**

**Rafael Filipe Vieira Reis**  
Serviço Nacional de Aprendizagem Industrial (SENAI MT)  
Cuiabá – MT – Brazil  
`[Seu e-mail aqui]`

**Abstract.** The transition from arithmetic reasoning to algebraic structuring demands abandoning calculus focused on discrete numeric values in favor of generalizing patterns. Computational Thinking acts as the mechanism to transpose this theoretical modeling into testable syntax. Based on Seymour Papert's Constructionism and the taxonomy by Weintrop et al. (2016), this paper highlights the empirical isomorphism between software architecture and formal logical foundations. The text advances on parametric decomposition as an essential analytical mechanism and proposes modeling Monte Carlo simulations in Python. We conclude that conditional propositions materialize in the code's semantics, forcing students to structure valid syllogisms.

**Resumo.** A passagem do raciocínio aritmético para a estruturação algébrica demanda o abandono do cálculo focado em valores numéricos discretos em favor da generalização de padrões. O Pensamento Computacional atua como o mecanismo de transposição dessa modelagem teórica. Fundamentando-se no Construcionismo de Papert e na taxonomia de Weintrop et al. (2016), este artigo evidencia o isomorfismo empírico entre a arquitetura de software e os fundamentos lógicos formais. O texto avança sobre a decomposição paramétrica como um mecanismo analítico essencial e propõe a modelagem de simulações de Monte Carlo em Python para o ensino de Probabilidade. A formulação de proposições condicionais materializa-se na semântica do código, obrigando o estudante a estruturar silogismos válidos.

## **1\. Introdução**

A passagem do raciocínio aritmético para a estruturação algébrica demanda o abandono do cálculo focado em valores numéricos discretos em favor da generalização de padrões. No cenário educacional, o Pensamento Computacional atua como o mecanismo de transposição dessa modelagem teórica para uma sintaxe testável. Ao codificar uma progressão em Python mediante o laço for i in range(n):, a variável n perde seu caráter estático, transformando-se em um parâmetro dinâmico em memória. Esse mapeamento direto entre a incógnita algébrica e o limite iterativo do laço instila significado empírico à generalização, permitindo visualizar como o dimensionamento escalar afeta o comportamento estrutural do algoritmo.  
Fundamentando-se no eixo de Práticas de Modelagem e Simulação descrito por \[Weintrop et al. 2016\], este artigo evidencia o isomorfismo empírico entre a arquitetura de software e os fundamentos lógicos formais. A construção de uma simulação computacional exige a aplicação estrita de conectivos lógicos inerentes às estruturas de controle de fluxo algorítmico (como *if/else*). Dessa forma, a formulação de proposições condicionais materializa-se na semântica do código, obrigando o estudante a estruturar silogismos válidos e a mapear tabelas de verdade com precisão para que o modelo estocástico atinja a consistência matemática pretendida.  
Para materializar essa proposta, o texto avança sobre a decomposição paramétrica como um mecanismo analítico essencial, no qual o estudante fraciona fenômenos probabilísticos em variáveis de estado isoladas. Ao estruturar simulações de Monte Carlo em Python, a infraestrutura da linguagem permite modelar a incerteza de maneira iterativa. Esse fracionamento une o design do código à inferência estatística, consolidando o entendimento de axiomas como a Lei dos Grandes Números a partir da convergência geométrica gerada pelos parâmetros definidos no modelo.

## **2\. Fundamentação Teórica**

### **2.1. Abstração e decomposição matemática**

O Pensamento Computacional exige a desconstrução estrutural do problema. A decomposição, sob a ótica matemática, ultrapassa a simples divisão de tarefas. Ao resolver o cálculo de volume de sólidos pelo método de fatiamento, a decomposição algorítmica exige que o estudante identifique os parâmetros invariáveis e os separe das variáveis iterativas, estruturando um laço de repetição acumulador.  
Paralelamente, a abstração computacional atua como um degrau direto para a abstração algébrica. Ao generalizar um valor fixo transformando-o em uma variável paramétrica, o estudante vivencia a mesma transição cognitiva necessária para compreender o papel de *x* na Álgebra. O computador exige que o aluno seja preciso na formulação das regras, promovendo um nível de rigor lógico audível imediatamente.

### **2.2. Modelagem e construcionismo**

A exigência de transformar ideias em código executável requer clareza operacional. Diferente da resolução no papel, o ambiente de desenvolvimento acusa falhas lógicas. Essa relação foi corroborada por \[Ng and Cui 2021\], observando como a criação de algoritmos promove ciclos contínuos de avaliação do próprio pensamento.  
Esse fenômeno baseia o Construcionismo de \[Papert 1980\], onde a tecnologia atinge seu ápice quando o estudante ensina a máquina a pensar. Ao programar, ele arquiteta seu modelo cognitivo e valida axiomas matemáticos através da mecânica do código.

## **3\. Metodologia**

Este estudo caracteriza-se como pesquisa bibliográfica exploratória qualitativa, incorporando as taxonomias de \[Weintrop et al. 2016\]. Articulando teoria educacional e engenharia de software, propõe-se um escopo empírico baseado em simulações em Python. A escolha justifica-se pela legibilidade sintática e aderência aos princípios matemáticos de estruturação algorítmica, materializando o ensino de Probabilidade em artefatos auditáveis.

## **4\. Aplicações Pedagógicas**

### **4.1. Aprendizagem baseada em problemas (ABP)**

Ao adotar a ABP, o professor instiga o desenvolvimento de algoritmos para desafios abertos. Conforme \[Rezende and Silva-Salse 2021\], a ABP é central para o pensamento crítico e transforma a matemática em uma ciência de investigação e design.

### **4.2. Simulação de Monte Carlo**

O estudante deve atuar como criador do modelo estocástico \[Wilensky 1995\]. Ao programar uma simulação para calcular uma aproximação de Pi em Python, vivencia-se a união entre geometria analítica e estatística inferencial.

`import random`

`def aproximar_pi_monte_carlo(pontos_totais):`  
    `pontos_no_circulo = 0`  
    `for _ in range(pontos_totais):`  
        `x, y = random.uniform(0, 1), random.uniform(0, 1)`  
        `if (x**2 + y**2) <= 1:`  
            `pontos_no_circulo += 1`  
              
    `return 4 * pontos_no_circulo / pontos_totais`

A compreensão do Teorema de Pitágoras e da proporção geométrica é a espinha dorsal do algoritmo, materializando o cruzamento entre Álgebra e Probabilidade.

### **4.3. Depuração (debugging)**

A depuração afasta a ideia punitiva do erro, reposicionando-o como refinamento científico. Divergências provocam a investigação de operadores e condições lógicas, auditando o raciocínio para diferenciar falhas sintáticas de semânticas.

## **5\. Resultados e Impactos Esperados**

**Tabela 1\. Diferenças paradigmáticas entre a abordagem tradicional e a instrução orientada ao PC**

| Dimensão Cognitiva | Ensino Tradicional | Apoiada pelo PC   |
| :---- | :---- | :---- |
| **Problemas** | Foco em fórmulas e substituição de valores. | Decomposição sistêmica e abstrações paramétricas. |
| **Erro** | Fracasso cognitivo; dedução de notas. | Evento de depuração; auditoria do modelo. |
| **Escalabilidade** | Amostras pequenas, dificultando visualizações. | Milhões de iterações (ex: Monte Carlo). |

## **6\. Considerações Finais**

O PC consolida-se como infraestrutura que viabiliza a execução da Lógica Matemática. A criação e depuração de código oferecem um ambiente científico onde abstrações ganham materialidade estrutural. Apoiada por \[Weintrop et al. 2016\], a disrupção metodológica reside em elevar o estudante a construtor do modelo cognitivo, substituindo o consumo de dogmas matemáticos pelo design algorítmico rigoroso.

## **Referências**

BARCELOS, T. et al (2015). Relações entre o Pensamento Computacional e a Matemática. In: WORKSHOPS DO CBIE, 4., Maceió. Anais \[...\]. SBC, p. 1369-1378.

BRASIL. Ministério da Educação (2018). Base Nacional Comum Curricular. Brasília: MEC.

CHAN, S. et al (2022). Tools and approaches for integrating computational thinking and mathematics. J. of Educational Computing Research, 60(8), p. 2036-2080.

NG, O.; CUI, Z. (2021). Examining primary students’ mathematical problem-solving in a programming context. ZDM – Mathematics Education, 53, p. 847-860.

PAPERT, S. (1980). Mindstorms: children, computers, and powerful ideas. NY: Basic Books.

REZENDE, A. A.; SILVA-SALSE, A. R. (2021). Utilização da ABP para o desenvolvimento do PC em Matemática. Educação Matemática Debate, 5(11), p. 1-21.

WEINTROP, D. et al (2016). Defining Computational Thinking for Mathematics and Science Classrooms. J. of Science Education and Technology, 25(1), p. 127-147.

WILENSKY, U. (1995). Learning probability through building computational models. In: CONF. ON THE PSYCHOLOGY OF MATH. EDUCATION, 19., Recife.

WING, J. M. (2006). Computational thinking. Communications of the ACM, 49(3), p. 33-35.

WISNIEWSKI, B. et al (2020). The power of feedback revisited. Frontiers in Psychology, 10\.