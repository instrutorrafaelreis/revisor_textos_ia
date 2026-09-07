# **O Pensamento Computacional como Ferramenta de Apoio ao Raciocínio Matemático**

### **Rafael Filipe Vieira Reis**

## **Resumo**

A transição do pensamento aritmético para a abstração algébrica impõe desafios cognitivos significativos na Educação Matemática. Neste cenário, o Pensamento Computacional (PC) emerge não apenas como um conjunto de habilidades técnicas, mas como uma infraestrutura epistemológica capaz de mediar e tornar observável essa transição. Este artigo investiga a sinergia entre as estruturas algorítmicas e o raciocínio matemático, distanciando-se de abordagens meramente utilitaristas. Fundamentando-se no Construcionismo de Seymour Papert e na taxonomia para a sala de aula de matemática e ciências de Weintrop et al. (2016), o estudo demonstra como práticas computacionais operam na construção de modelos mentais complexos. O texto aprofunda a aplicação matemática da decomposição e da abstração paramétrica e propõe, metodologicamente, a modelagem de simulações do método de Monte Carlo em linguagem Python para o ensino de Probabilidade. Conclui-se que o desenvolvimento e a depuração de algoritmos oferecem um ambiente rigoroso no qual a Lógica Matemática se torna executável, permitindo ao estudante investigar hipóteses ativamente e consolidar o pensamento analítico estruturado.  
**Palavras-chave:** Pensamento Computacional; Lógica Matemática; Construcionismo; Simulações em Python; Modelagem Epistemológica.

## **1\. Introdução**

A transição da aritmética para a álgebra exige que o estudante migre do cálculo numérico particular para a generalização estrutural. Práticas pedagógicas tradicionais, contudo, tendem a dogmatizar essa passagem por meio de axiomas abstratos descontextualizados. Nesse cenário, o Pensamento Computacional (PC) surge como um registro de representação dinâmico, onde variáveis de memória e estruturas de controle (como laços e condicionais) tornam visíveis e manipuláveis os parâmetros algébricos antes abstratos.  
Em vez de confinar o uso do computador à interação passiva com simulações no formato "caixa-preta", a integração conceitual entre Matemática e Computação exige que o aprendiz atue como projetista do modelo lógico. Essa premissa fundamenta-se na epistemologia construcionista de Seymour Papert, que postula que a aprendizagem matemática ocorre com maior eficácia cognitiva quando o estudante utiliza a linguagem de programação para construir artefatos computáveis, externalizando e depurando seu próprio raciocínio. Embora o conceito contemporâneo de PC tenha sido amplamente catalisado por Jeannette Wing (2006) como uma competência transversal, o avanço da área exige superar a superficialidade enciclopédica dessa definição inicial. Autores como Weintrop et al. (2016) oferecem uma taxonomia rigorosa especificamente voltada para as disciplinas de exatas, categorizando o PC em práticas de modelagem e simulação, uso de dados e investigação de sistemas. É sob essa lente taxonômica rigorosa que os algoritmos encontram paralelos estruturais com os conectivos, proposições e condicionais da Lógica Matemática.  
Para materializar essa sinergia metodológica, este artigo adota um escopo empírico-aplicado claro: a exploração de simulações do método de Monte Carlo, desenvolvidas em linguagem Python, voltadas ao ensino prático de Probabilidade. A escolha dessa linguagem e deste objeto matemático ilustra de maneira tangível como o desenvolvimento de scripts exige do estudante a decomposição meticulosa de variáveis estocásticas e a formalização do espaço amostral. Assim, o objetivo central deste estudo é investigar como a modelagem computacional ativa e a depuração de código atuam como vetores de aprofundamento da abstração algébrica e da validação de hipóteses matemáticas.

## **2\. Fundamentação Teórica**

### **2.1 Aprofundamento Epistemológico: Abstração e Decomposição Matemática**

O Pensamento Computacional não se reduz à tradução de fórmulas matemáticas para linhas de código; ele exige a desconstrução epistemológica do problema. A decomposição e a abstração, pilares do PC, adquirem contornos altamente específicos quando aplicados ao raciocínio lógico-matemático.  
A decomposição, sob a ótica matemática, ultrapassa a aplicação instrumental de etapas administrativas. Ao abordar a simulação de Monte Carlo para estimar a probabilidade de um evento, a decomposição algorítmica exige que o estudante explicite o espaço amostral, defina as variáveis de entrada e estruture a contabilização de sucessos em uma rotina iterativa. A parametrização do número total de simulações (N) materializa a transição da aritmética concreta para a generalização algébrica: ao manipular N e observar o comportamento da estimativa conforme N tende ao infinito, o aluno apreende o conceito de limite probabilístico e convergência estocástica em uma estrutura algorítmica observável.  
Paralelamente, a abstração computacional atua como um degrau direto para a abstração algébrica. Na programação, ao generalizar um valor numérico fixo transformando-o em uma variável paramétrica ou em uma função modular, o estudante vivencia exatamente a mesma transição cognitiva necessária para compreender o papel de x ou f(x) na Álgebra. Ao desenvolver um algoritmo em Python para gerar distribuições estatísticas, por exemplo, o estudante constata que os mesmos parâmetros lógicos que regem o sorteio de cartas de um baralho podem ser abstraídos para prever a probabilidade de eventos complexos. O computador não resolve o problema pelo aluno; ele exige que o aluno seja preciso e semanticamente correto na formulação das regras, promovendo um nível de rigor lógico que o ambiente puramente manuscrito muitas vezes não consegue auditar de forma imediata.

### **2.2 Pensamento Matemático, Modelagem e Construcionismo**

A exigência de transformar ideias matemáticas em código executável requer clareza operacional que não permite ambiguidades. Diferente da resolução no papel, onde saltos lógicos podem ser ofuscados ou ignorados, o ambiente de desenvolvimento acusa falhas na estruturação do raciocínio. A relação entre a programação e a modelagem matemática foi corroborada por Ng e Cui (2021), que observaram como a criação de algoritmos impulsiona a utilização de variáveis e promove ciclos contínuos de avaliação do próprio pensamento.  
Esse fenômeno é a base do Construcionismo. Para Papert, a tecnologia educacional atinge seu ápice quando o estudante ensina a máquina a pensar. Ao programar, o estudante está, de fato, arquitetando seu próprio modelo cognitivo, validando axiomas matemáticos através da mecânica do código. Essa abordagem muda o foco da obtenção da resposta correta para a arquitetura do processo que gera a resposta.

## **3\. Metodologia**

Este estudo caracteriza-se como uma pesquisa bibliográfica exploratória de abordagem qualitativa, fundamentada na revisão crítica da literatura sobre Educação Matemática e Pensamento Computacional. A análise transcende as definições clássicas, incorporando as taxonomias propostas por Weintrop et al. (2016) e a fundamentação epistemológica do Construcionismo.  
Como diferencial metodológico, este trabalho articula a teoria educacional com a engenharia de software aplicada à sala de aula, propondo um escopo empírico baseado no desenvolvimento de simulações matemáticas em Python. Essa escolha se justifica pela legibilidade da sintaxe de Python e por sua aderência aos princípios matemáticos de estruturação algorítmica, permitindo materializar conceitos teóricos — especificamente o ensino de Probabilidade via simulação de Monte Carlo — em artefatos testáveis e auditáveis.

## **4\. Aplicações Pedagógicas**

### **4.1 Aprendizagem Baseada em Problemas (ABP) na Lógica Algorítmica**

A integração do PC exige que a atividade didática migre da exposição passiva para o protagonismo estruturado. Ao adotar a Aprendizagem Baseada em Problemas (ABP), o professor instiga os estudantes a desenvolver algoritmos para solucionar desafios abertos, como a otimização de rotas ou modelagem financeira. Conforme argumentado por Rezende e Silva-Salse (2021), a ABP é central para o pensamento crítico, e, quando aliada ao PC, transforma a matemática de uma disciplina de verificação em uma ciência de investigação e design.

### **4.2 Simulações Computacionais e Probabilidade: O Método de Monte Carlo**

A Probabilidade é historicamente um dos ramos matemáticos mais beneficiados pela capacidade computacional. Em vez de limitar o aprendizado a fórmulas combinatórias descontextualizadas, o estudante deve atuar como criador do modelo estocástico. Wilensky (1995) defende que construir modelos computacionais é a principal forma de dar sentido a conceitos como aleatoriedade e Lei dos Grandes Números.  
Uma das aplicações mais robustas desse conceito é a implementação do Método de Monte Carlo. À luz da Teoria dos Registros de Representação Semiótica de Raymond Duval, a passagem da fórmula clássica da probabilidade P(A) \= n(A)/n(Ω) para o script em Python configura uma conversão entre registros semióticos distintos. O estudante realiza o tratamento no registro algorítmico ao definir variáveis, laços e condicionais que simulam os ensaios estocásticos. Ao programar uma simulação em Python para calcular uma aproximação de Pi através do lançamento de pontos aleatórios em um plano cartesiano, o aluno vivencia a união entre geometria analítica e estatística inferencial.

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

Neste código, a compreensão do Teorema de Pitágoras e da proporção geométrica de áreas é a espinha dorsal do algoritmo. A máquina atua apenas como o executor veloz; o intelecto matemático reside no design da função, materializando o cruzamento entre Álgebra e Probabilidade.

### **4.3 Depuração (Debugging) como Epistemologia do Erro**

A depuração ou debugging afasta a ideia punitiva do erro matemático e o reposiciona como uma etapa científica de refinamento de hipóteses. Quando o resultado de uma função diverge do esperado, o estudante é provocado a investigar a hierarquia de operadores, as condições lógicas e os tipos de dados. Esse processo audita o raciocínio matemático passo a passo. A correção do bug exige reflexão epistemológica: o erro é sintático (um parêntese esquecido) ou semântico (uma falha na própria equação formulada)?

## **5\. Resultados e Impactos Esperados**

A transição para um modelo educacional mediado pelo Pensamento Computacional gera impactos quantificáveis e qualitativos na apreensão da matemática. Para sistematizar essa evolução, a tabela abaixo evidencia as diferenças paradigmáticas entre a abordagem tradicional e a instrução orientada ao PC.

| Dimensão Cognitiva | Ensino Matemático Tradicional | Abordagem Apoiada pelo Pensamento Computacional |
| :---- | :---- | :---- |
| Tratamento de Problemas | Foco na busca pela fórmula correta e substituição de valores para encontrar um resultado estático. | Foco na decomposição sistêmica, modelagem iterativa e criação de abstrações paramétricas. |
| Status do Erro | Visto como fracasso cognitivo; resulta em dedução de notas e reforço da repetição manual. | Visto como evento de depuração lógica (debugging); exige auditoria do modelo e refatoração de hipóteses. |
| Escalabilidade de Dados | Limitada a amostras muito pequenas, dificultando a visualização de tendências probabilísticas e estatísticas. | Capacidade de iterar milhões de ciclos (ex: método de Monte Carlo), consolidando a Lei dos Grandes Números empiricamente. |

## **6\. Considerações Finais**

O Pensamento Computacional atua como muito mais do que um mero recurso utilitário para automatizar contas. Ele se consolida como uma infraestrutura de pensamento que viabiliza a execução da Lógica Matemática. A criação, manipulação e depuração de código oferecem um ambiente científico de experimentação no qual as abstrações matemáticas ganham materialidade estrutural. Como demonstrado através da aplicação de simulações estocásticas em Python e apoiado pela taxonomia de Weintrop et al. (2016), a verdadeira disrupção metodológica reside em elevar o estudante à categoria de construtor do modelo cognitivo, substituindo o consumo de dogmas matemáticos pelo design algorítmico rigoroso.

## **Referências**

> * BARCELOS, Thiago; MUÑOZ, Roberto; ACEVEDO, Rodolfo Villarroel; SILVEIRA, Ismar Frango. Relações entre o Pensamento Computacional e a Matemática: uma revisão sistemática da literatura. Anais dos Workshops do Congresso Brasileiro de Informática na Educação, 2015\. DOI: 10.5753/cbie.wcbie.2015.1369.  
> * BRASIL. Ministério da Educação. Base Nacional Comum Curricular. Brasília, DF: MEC, 2018\.  
> * CHAN, Shiau-Wei; LOOI, Chee-Kit; HO, Weng Kin; KIM, Mi Song et al. Tools and approaches for integrating computational thinking and mathematics: a scoping review of current empirical studies. Journal of Educational Computing Research, v. 60, n. 8, p. 2036–2080, 2022/2023. DOI: 10.1177/07356331221098793.  
> * NG, Oi-Lam; CUI, Zhihao. Examining primary students’ mathematical problem-solving in a programming context: towards computationally enhanced mathematics education. ZDM – Mathematics Education, v. 53, p. 847–860, 2021\. DOI: 10.1007/s11858-020-01200-7.  
> * PAPERT, Seymour. Mindstorms: Children, Computers, and Powerful Ideas. Basic Books, 1980\.  
> * REZENDE, Adriano Alves de; SILVA-SALSE, Angela Ruth. Utilização da aprendizagem baseada em problemas (ABP) para o desenvolvimento do pensamento crítico (PC) em Matemática: uma revisão teórica. Educação Matemática Debate, v. 5, n. 11, p. 1–21, 2021\. DOI: 10.46551/emd.e202111.  
> * WEINTROP, David; BEHESHTI, Elham; HORN, Michael; ORTON, Kai; JUGO, Kemi; TROUT, Jason; WILENSKY, Uri. Defining Computational Thinking for Mathematics and Science Classrooms. Journal of Science Education and Technology, v. 25, n. 1, p. 127-147, 2016\. DOI: 10.1007/s10956-015-9581-5.  
> * WILENSKY, Uri. Learning probability through building computational models. In: Proceedings of the Nineteenth International Conference on the Psychology of Mathematics Education. Recife, 1995\.  
> * WING, Jeannette M. Computational thinking. Communications of the ACM, v. 49, n. 3, p. 33–35, 2006\. DOI: 10.1145/1118178.1118215.  
> * WISNIEWSKI, Benedikt; ZIERER, Klaus; HATTIE, John. The power of feedback revisited: a meta-analysis of educational feedback research. Frontiers in Psychology, v. 10, artigo 3087, 2020\. DOI: 10.3389/fpsyg.2019.03087.